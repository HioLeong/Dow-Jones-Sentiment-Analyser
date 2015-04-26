import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;

import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

import com.csvreader.CsvWriter;

public class PreProcessing {

	public static void main(String[] args) {
		for (int i = 1; i < 63; i++) {
			readFileByLine("T" + i);
		}

	}

	private static void readFileByLine(String filename) {
		try {
			File fin = new File("/Users/tinafallahi/tweets/" + filename);
			FileInputStream fis = new FileInputStream(fin);

			BufferedReader br = new BufferedReader(new InputStreamReader(fis));

			String line = null;
			while ((line = br.readLine()) != null) {
				divideTweets(line);
			}

			br.close();

			System.out.println("DONE: " + filename);
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

	private static void divideTweets(String line) {
		String[] tweets = line.split("\\{\"created\\_at\"\\:");
		for (int i = 0; i < tweets.length; i++) {
			getJSONObjects("{\"created_at\":" + tweets[i]);
		}
	}

	private static void getJSONObjects(String tweet) {
		JSONObject json;
		try {
			json = (JSONObject) new JSONParser().parse(tweet);
			filterTweets(json);
		} catch (ParseException e) {
			e.printStackTrace();
		}
	}

	private static void filterTweets(JSONObject json) {
		try {
			if (json.get("lang").toString().equals("en")) {
				String userString = json.get("user").toString();
				JSONObject user = (JSONObject) new JSONParser().parse(userString);
				int followers = Integer.parseInt(user.get("followers_count").toString());
				int statuses = Integer.parseInt(user.get("statuses_count").toString());
				if(followers > 20 && statuses>20) {
					int favourites = Integer.parseInt(json.get("favorite_count").toString()); 
					int retweets = Integer.parseInt(json.get("retweet_count").toString());
					//if(favourites>0 && retweets>0) {
						String[] words = json.get("text").toString().split(" ");
						if(words.length > 3) {
							writeTweetsToCSV(json);
						}
					//}
				}
			}
		} catch (ParseException e) {
			e.printStackTrace();
		} catch (NullPointerException e) {
			e.printStackTrace();
		}

	}

	private static void writeTweetsToCSV(JSONObject json) {
		String outputFile = "/Users/tinafallahi/tweets/tweets.csv";

		boolean alreadyExists = new File(outputFile).exists();

		try {
			CsvWriter csvOutput = new CsvWriter(
					new FileWriter(outputFile, true), ',');

			if (!alreadyExists) {
				csvOutput.write("company");
				csvOutput.write("created_at");
				csvOutput.write("text");
				csvOutput.write("hashtags");
				csvOutput.write("symbols");
				csvOutput.write("urls");
				csvOutput.write("mentions");
				csvOutput.endRecord();
			}
			
			String tweetBody = json.get("text").toString();
			if(tweetBody.toLowerCase().contains("coca cola") || tweetBody.toLowerCase().contains("coca-cola")) {
				csvOutput.write("coca cola");
			} else if(tweetBody.toLowerCase().contains("chevron")) {
				csvOutput.write("chevron");
			} else if(tweetBody.toLowerCase().contains("exxon")) {
				csvOutput.write("exxon");
			} else {
				return;
			}
			csvOutput.write(json.get("created_at").toString());
			csvOutput.write(tweetBody);
			String entitiesString = json.get("entities").toString();
			JSONObject entities = (JSONObject) new JSONParser().parse(entitiesString);
			csvOutput.write(entities.get("hashtags").toString());
			csvOutput.write(entities.get("symbols").toString());
			csvOutput.write(entities.get("urls").toString());
			csvOutput.write(entities.get("user_mentions").toString());
			csvOutput.endRecord();

			csvOutput.close();
		} catch (IOException e) {
			e.printStackTrace();
		} catch (ParseException e) {
			e.printStackTrace();
		} catch (NullPointerException e) {
			e.printStackTrace();
		}
	}
}
