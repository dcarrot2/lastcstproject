package com.example.pollmap;

import java.util.ArrayList;
import java.util.List;

import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.StringEntity;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.message.BasicHeader;
import org.apache.http.params.HttpConnectionParams;
import org.apache.http.protocol.HTTP;
import org.json.JSONObject;

import android.support.v7.app.ActionBarActivity;
import android.support.v7.app.ActionBar;
import android.support.v7.appcompat.R.id;
import android.support.v4.app.Fragment;
import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.view.View.OnClickListener;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.EditText;
import android.os.Build;



public class Poll extends Activity {
	
//VARIABLE DECLARATIONS
	private static final String TAG = "VoteActivity";
	public static String country;
	Button btn;
	EditText t1;
	EditText t2;
	static List<String> myItems = new ArrayList<String>();
	static List<String> myCountry = new ArrayList<String>();

	
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_poll);
		//gets button ID
		btn = (Button)findViewById(R.id.button1);
		//gets edittext id
		final EditText t1 = (EditText)findViewById(R.id.editText1);
		//gets editttext id of edit text 2
		final EditText t2 = (EditText)findViewById(R.id.editText2);
		//set an on click listener for the submit button
		btn.setOnClickListener(new OnClickListener() {
			
			@Override
			public void onClick(View v) {
				// TODO Auto-generated method stub
				//converts the submitted text into strings
				String name = t1.getText().toString();
				country = t2.getText().toString();
				//adds strings to appropriate list
				myCountry.add(country);
				myItems.add(name);
				//sends the JSON
				sendJson(country, name);
				//returns to nameList activity
				Intent intent = new Intent(Poll.this, NameList.class);
				startActivity(intent);
				//finish so that you cannot return to page
				finish();
				
			}
		});
		
		
	}

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {

		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.poll, menu);
		return true;
	}

	@Override
	public boolean onOptionsItemSelected(MenuItem item) {
		// Handle action bar item clicks here. The action bar will
		// automatically handle clicks on the Home/Up button, so long
		// as you specify a parent activity in AndroidManifest.xml.
		int id = item.getItemId();
		if (id == R.id.action_settings) {
			return true;
		}
		return super.onOptionsItemSelected(item);
	}

	//function to send the json object to the webapp through the designated IP
	public void sendJson(final String status, final String name) {
		Thread t = new Thread() {

			public void run() {
				HttpClient client = new DefaultHttpClient();
				HttpConnectionParams.setConnectionTimeout(client.getParams(), 10000); //Timeout Limit
				//HttpResponse response;
	            JSONObject json = new JSONObject();

	            try {
	            	HttpPost post = new HttpPost("http://10.11.177.99:8000/polls/1/voteandroid/");
	            	json.put("choice", status);
	            	json.put("Name", name);
	            	StringEntity se = new StringEntity( json.toString());  
	            	se.setContentType(new BasicHeader(HTTP.CONTENT_TYPE, "application/json"));
	            	post.setEntity(se);
	            	//HttpResponse response = 
	            			client.execute(post);
	            	Log.d(TAG, "JSON file posted");
         

	            } catch(Exception e) {
	            	e.printStackTrace();
	            	//logs to track if connection was established
	            	Log.d(TAG, "Caught Exception");
	            	Log.d(TAG, "Cannot Establish Connection");
	            }

			}
		};
		t.start();      
	}
}