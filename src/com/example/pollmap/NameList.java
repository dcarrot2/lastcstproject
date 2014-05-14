package com.example.pollmap;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.UnsupportedEncodingException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import org.apache.http.HttpEntity;
import org.apache.http.HttpResponse;
import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.params.HttpConnectionParams;
import org.json.JSONObject;

import android.support.v7.app.ActionBarActivity;
import android.support.v7.app.ActionBar;
import android.support.v4.app.Fragment;
import android.app.ListActivity;
import android.content.Intent;
import android.os.AsyncTask;
import android.os.Bundle;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.Menu;
import android.view.MenuInflater;
import android.view.MenuItem;
import android.view.View;
import android.view.ViewGroup;
import android.widget.AdapterView;
import android.widget.AdapterView.OnItemClickListener;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.Toast;
import android.os.Build;

public class NameList extends ListActivity {
	
	private static final String TAG = "VoteActivity";
	static int namep; //position of name clicked
	static InputStream is = null;
    static JSONObject jObj = null;
    static String jsonin = "";
    String tempN;
    String tempC;
    
    //a list of all the countries on Earth
    List<String> checks = new ArrayList<String> (Arrays.asList("Afghanistan","Albania","Algeria","Andorra","Angola","Antigua and Barbuda",
    	     "Argentina","Armenia","Aruba","Australia","Austria","Azerbaijan",
    	     "Bahamas","Bahrain","Bangladesh","Barbados","Belarus","Belgium","Belize",
    	     "Benin","Bhutan","Bolivia","Bosnia and Herzegovina","Botswana","Brazil",
    	     "Brunei","Bulgaria","Burkina Faso","Burma","Burundi","Canada",
    	     "Cambodia","Cameroon","Cape Verde","Central African Republic","Chad",
    	     "Chile","China","Colombia","Comoros","Democratic Republic of the Congo",
    	     "Republic of the Congo","Costa Rica","Cote d'Ivoire","Croatia","Cuba",
    	     "Curacao","Cyprus","Czech Republic","Denmark","Djibouti","Dominica",
    	     "Dominican Republic","East Timor","Ecuador","Egypt","El Salvador","Equatorial Guinea",
    	     "Eritrea","Estonia","Ethiopia","Fiji","Finland","France","Gabon",
    	     "The Gambia","Georgia","Germany","Ghana","Greece","Grenada","Guatemala",
    	     "Guinea","Guinea-Bissau","Guyana","Haiti","Holy See","Honduras","Hong Kong",
    	     "Hungary","Iceland","India","Indonesia","Iran","Iraq","Ireland","Isreal","Italy",
    	     "Jamaica","Japan","Jordan","Kazakhstan","Kenya","Kiribati","North Korea","South Korea",
    	     "Kosovo","Kuwait","Kyrgyzstan","Laos","Latvia","Lebanon","Lesotho","Liberia",
    	     "Libya","Liechtenstein","Lithuania","Luxembourg","Macau","Macedonia","Madagascar",
    	     "Malawi", "Malaysia","Maldives","Mali","Malta","Marshall Islands","Mauritania",
    	     "Mauritius","Mexico","Micronesia","Moldova","Monaco","Mongolia","Montenegro","Morocco",
    	     "Mozambique","Namibia","Nauru","Nepal","Netherlands","Netherlands Antilles","New Zealand",
    	     "Nicaragua","Niger","Nigeria","North Korea","Norway","Oman","Pakistan","Palau",
    	     "Palestinian Territories","Panama","Papua New Guinea","Paraguay","Peru","Philippines",
    	     "Poland","Portugal","Qatar","Romania","Russia","Rwanda","Saint Kitts and Nevis",
    	     "Saint Lucia","Saint Vincent and the Grenadines","Samoa","San Marino","Sao Tome and Principe",
    	     "Saudi Arabia","Senegal","Serbia","Seychelles","Sierra Leone","Singapore","Sint Maarten",
    	     "Slovakia","Slovenia","Solomon Islands","Somalia","South Africa","South Korea","South Sudan",
    	     "Spain","Sri Lanka","Sudan","Suriname","Swaziland","Sweden","Switzerland","Syria",
    	     "Taiwan","Tajikistan","Tanzania","Thailand","Timor-Leste","Togo","Tonga","Trinidad and Tobago",
    	     "Tunisia","Turkey","Turkmenistan","Tuvalu","Uganda","Ukraine","United Arab Emirates",
    	     "United Kingdom","United States","Uruguay","Uzbekistan","Vanuatu","Venezuela","Vietnam","Yemen",
    	     "Zambia","Zimbabwe"));
    
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
	
		
		//creates adapter for the list view
		ArrayAdapter<String> adapter = new ArrayAdapter<String>(this,android.R.layout.simple_list_item_1,
				Poll.myItems);
		//sets the list adapter to display the list view
		setListAdapter(adapter);
		//calls the function to retrieve the JSON object
		new ResultsUpdate().execute();
		
		//counter to keep track of amount of items in DB
		int counter = 0;
		
		for( int i=0; i< jsonin.length(); i++ ) {
		    if( jsonin.charAt(i) == ',' ) {
		        counter++;
		    } 
		}
		
		if(jsonin!="")
		{
			String[] array = jsonin.split(",");
			String tempString;
			String[] tempArray;
			
			for(int x = 0; x <= counter; x++)
			{
				tempString = array[x].substring(7,array[x].length()-1);
				tempArray = tempString.split(" ");
				//if user submits only first name and one word country
				if (tempArray.length==2)
				{
					if(Poll.myItems.contains(tempArray[0]))
					{
						continue;
					}
					else
					{
						Poll.myItems.add(tempArray[0]);
						Poll.myCountry.add(tempArray[1]);
					}
				}
				//if user submits either one word name and 2 word country, or
				//submits two word name and 1 word country
				else if(tempArray.length == 3)
				{
					String temp = tempArray[1] + " " + tempArray[2];
					if(checks.contains(temp))
					{
						if(Poll.myItems.contains(tempArray[0]))
							continue;
						else
						{
							
							Poll.myItems.add(tempArray[0]);
							Poll.myCountry.add(tempArray[1]+ " " + tempArray[2]);
						}
					}
					
					else
					{
						if(Poll.myItems.contains(tempArray[0] + " " + tempArray[1]))
							continue;
						else
						{
							
							Poll.myItems.add(tempArray[0] + " " + tempArray[1]);
							Poll.myCountry.add(tempArray[2]);
						}
					}
				}	
				//if user submits name and last name with two word country
				else if(tempArray.length == 4)
				{
					if(Poll.myItems.contains(tempArray[0] + " " + tempArray[1]))
						continue;
					else
					{
						Poll.myItems.add(tempArray[0] + " " + tempArray[1]);
						Poll.myCountry.add(tempArray[2] + " " + tempArray[3]);
					}
					
				}
			}
			
			
		}
		
		
		
	}
	
	//retrieves results from webapp
	class ResultsUpdate extends AsyncTask<Void, Void, String>
	{  
	
//		@Override 
//		protected void onProgressUpdate(Void... values) {
//			super.onProgressUpdate(values);
//			Toast.makeText(NameList.this, "Update in progress",Toast.LENGTH_LONG).show();
//		}
//
//		@Override 
//		protected void onPostExecute(String result) { 
//			Log.d(TAG, "Post Execute Started");
//		}
		@Override
		protected String doInBackground(Void... params) {
			Log.d(TAG, "Do In Background Started");
			try {
				jsonin =getJson();
				return "";
			} catch (Exception e) {
				Log.e(TAG, "Caught Exception");
				e.printStackTrace();
				return "";
			}
		}
	}
	
	@Override
	//sets up an on item click listener to get launch map acitivty when item is clicked
	protected void onListItemClick(ListView l, View v, int position, long id) {
		//gets position
		namep = position;
		Intent intent = new Intent(this, MainActivity.class);
		startActivity(intent);
	}

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
	    // Inflate the menu items for use in the action bar
	    MenuInflater inflater = getMenuInflater();
	    inflater.inflate(R.menu.name_list, menu);
	    return super.onCreateOptionsMenu(menu);
	}
	
	@Override
	public boolean onOptionsItemSelected(MenuItem item) {
	    // Handle presses on the action bar items
	    switch (item.getItemId()) {
	        case R.id.action_new:
	        	//adds new poll to namelist
	        	Intent intent = new Intent(this, Poll.class);
	        	startActivity(intent);
	            return true;
	        case R.id.action_refresh:
	        	//refreshes names
	        	finish();
	        	startActivity(getIntent());
	        	return true;
	       
	        default:
	            return super.onOptionsItemSelected(item);
	    }
	}

	//retrieves the json object by connecting to webapp
	//along with provides logs on whether an exception was thrown
	public String getJson() {				
		HttpClient client = new DefaultHttpClient();
		HttpConnectionParams.setConnectionTimeout(client.getParams(), 10000); //Timeout Limit
		try {
			//ip of webapp
			HttpPost post = new HttpPost("http://10.11.177.99:8000/polls/1/sendandroidnames/");
			HttpResponse httpResponse = client.execute(post);
			HttpEntity httpEntity = httpResponse.getEntity();
			is = httpEntity.getContent();          
			Log.d(TAG, "Got Content from Entity");
           //lists of exceptions
		} catch (UnsupportedEncodingException e) {
			Log.d(TAG, "Caught Exception");
			e.printStackTrace();
		} catch (ClientProtocolException e) {
			Log.d(TAG, "Caught Exception");
			e.printStackTrace();
		} catch (IOException e) {
			Log.d(TAG, "Caught Exception");
			e.printStackTrace();
		}
         
		try {
			//inputsteamreader decondes into 8 single-byte graphic characters
			//and the buffreader reads the text from the input stream
			BufferedReader reader = new BufferedReader(new InputStreamReader(is, "iso-8859-1"), 8);
			StringBuilder sb = new StringBuilder();
			String line = null;
			while ((line = reader.readLine()) != null) {
				sb.append(line + "\n");
			}
			is.close();
			jsonin = sb.toString();
			Log.d(TAG, "String created");
		} catch (Exception e) {
			Log.d(TAG, "Caught Exception");
			Log.e("Buffer Error", "Error converting result " + e.toString());
		}
		Log.d(TAG, "Json String returned");
		return jsonin;
    }

}
