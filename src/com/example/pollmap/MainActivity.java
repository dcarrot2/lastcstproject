package com.example.pollmap;

import java.io.IOException;
import java.util.List;

import android.app.Activity;
import android.location.Geocoder;
import android.os.Bundle;
import android.os.Handler;
import android.support.v7.app.ActionBarActivity;
import android.view.Menu;
import android.view.MenuItem;
import android.widget.Toast;

import com.google.android.gms.identity.intents.Address;
import com.google.android.gms.maps.CameraUpdate;
import com.google.android.gms.maps.CameraUpdateFactory;
import com.google.android.gms.maps.GoogleMap;
import com.google.android.gms.maps.MapFragment;
import com.google.android.gms.maps.model.LatLng;
import com.google.android.gms.maps.model.Marker;
import com.google.android.gms.maps.model.MarkerOptions;

public class MainActivity extends Activity{
	
//VARIABLE DECLARATIONS
	//declare an object of the GoogleMap class
	GoogleMap map;
	//double for latitude
	double lat;
	//double for longitude
	double lng;
	//string to hold the country's title
	String place;
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);
		
		//gets the id of the map fragment
		map = ((MapFragment) getFragmentManager().findFragmentById(R.id.map)).getMap();
		
		//declares a new geocoder object
		Geocoder gc = new Geocoder(this);
		try {
			//creates a list containing all associated addresses with the inputted country,
			//and chooses the very first one of that list
			List<android.location.Address> list = gc.getFromLocationName(Poll.myCountry.get(NameList.namep), 1);
			android.location.Address add = list.get(0);
			//gets the latitude of country
			lat = add.getLatitude();
			//gets the longitude of country 
			lng = add.getLongitude();
			//gets the name of selected country from list which returns a string
			place = add.getCountryName();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		
		//A cameraupdate is set up to zoom in a total of four times
		CameraUpdate update = CameraUpdateFactory.newLatLngZoom(new LatLng(lat, lng), 4);
		map.animateCamera(update);
		//sets up a marker on the map with the title of the place and name of who selected it
		final Marker marker = map.addMarker(new MarkerOptions().position(new LatLng(lat, lng)).title(place)
				.snippet(Poll.myItems.get(NameList.namep)));
		
		//set up handler to delay info window from appearing at start
		Handler handler = new Handler();

		//runnable set up to hold code which will fun after the handler
		Runnable r = new Runnable() {
			
			@Override
			public void run() {
				//display info window
				marker.showInfoWindow();
			}
		};
		
		//call handler
		handler.postDelayed(r, 1000);
		
	}
		
	

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {

		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.main, menu);
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

}
