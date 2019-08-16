<!DOCTYPE HTML>
<html>
<head>
	<meta charset="utf-8">
</head>
<h1>Using Mallet to Model Landtalk Data</h1>
<p>(These instructions are distilled and made as specific as possible for the LandTalk project, but if these instructions are unclear or overly distilled, all the information can be found <a href= "https://programminghistorian.org/en/lessons/topic-modeling-and-mallet#your-first-topic-model)">here.</a> <em>Instructions differ slightly on windows (primarily backslashes instead of forward-slashes)</em></p>
<h2>Setting Up</h2>
<ul>
	<li>Download the <em>transcripts</em> file from the shared Google Drive (Ask Erik or Deborah for access). 
		<ul>
			<li>This will give you a zip file with all the transcripts produced by users across all conversations for which we have transcripts available. More generally, any collection of text files will work in place of this file, should we need to model any other corpus. <b>Note:</b> Although using only the transcripts leaves out data from the responses entered by the users, the user responses are (or at least should be) based on the transcripts. The following procedure is based on the assumption that this is sufficient information to produce a robust topic model since, as of the time of this writing, it is our most efficient means of obtaining clean data.</li>
		</ul>
	</li><br>
	<li>If you have not done so already, download <a href = "http://mallet.cs.umass.edu/download.php"> MALLET </a> and the <a href="https://www.oracle.com/technetwork/java/javase/downloads/index.html"> Java Developer's Kit (JDK)</a>. Unzip Mallet somewhere you will find it (such as your desktop) and you will now have a directory called <kbd>mallet-2.0.8</kbd>. It's in your best interest to just rename this file <kbd>mallet</kbd>.</li><br>
	<li>At this point, open up your terminal and navigate to the <kbd>mallet</kbd> directory (using the <code>cd</code> command).</li><br>
	<li>Unzip the transcripts file and copy or move the folder into the <kbd>mallet</kbd> folder</li><br>
	<li>Type in <code>./bin/mallet</code> and if a list of commands appears, you've installed mallet correctly.</li><br>
</ul>

<h2>Typing in MALLET Commands</h2>
<ul>
	<li>Use <code>bin/mallet import-dir --help</code> to see a list of options you can use to tweak the output of your data.</li><br>
	<li>The following command can be performed on either any file in the <kbd>sample-data</kbd> folder or on your own data file. I recommend looking through the <kbd>sample-data</kbd> folder to become familiar with what's in it. This folder contains a number of <kbd>.txt</kbd> files, each folder containing these <kbd>.txt</kbd> files can be considered a corpus of data. These will be the equivalent of our <kbd>transcripts</kbd> folder. This folder will be useful for testing different flags and becoming familiar with the MALLET workflow.
		<ul><br>
			<li>Try entering the following command in your terminal: <br><br> <code>bin/mallet import-dir --input sample-data/web/en --output tutorial.mallet --keep-sequence --remove-stopwords</code> <br><br> This command imports a specific directory, turns it into a MALLET file, keeps the original texts in the order they were listed, and strips out stop words such as and, the, but, and if that would otherwise obstruct analysis using the default stop-words dictionary.</li>
		</ul>
	</li><br>
	<li> In this example, the <kbd>sample-data</kbd> folder is used, this should be replaced with the transcripts folder or any other corpus you would like to analyze. This then spits out a file called <kbd>tutorial.mallet</kbd> but you should not name your file 'tutorial' when running the command on your own corpus. This file can now be found in the mallet directory and contains your data in a format MALLET can manipulate.</li><br>
</ul>

<h2>Producing a Topic Model</h2>
<ul>
	<li>At the command prompt, from within the <code>mallet</code> directory, the following command will produce 3 output files with relevant data:<br><code>bin\mallet train-topics  --input tutorial.mallet --num-topics 20 --output-state topic-state.gz --output-topic-keys tutorial_keys.txt --output-doc-topics tutorial_compostion.txt </code></li><br>
	<li>The <kbd>topic-state.gz</kbd>, <kbd>tutorial_keys.txt</kbd>, and <kbd>tutorial_composition.txt</kbd> files will be your output files, you can rename these as you wish. The command we just ran should have opened up the <kbd>tutorial.mallet</kbd> file, trained it to find 20 topics <em>(this number can be changed as needed)</em> and produced the three aforementioned output files.</li><br>
	<li><b>Some notes on the output files: </b><br>
		<ul>
			<li>The <kbd>.gz</kbd> file will output every word in your corpus, the file it belongs to, and the topic it has been assigned to (topics are numbered 0-19 for 20 topics).</li><br>
			<li>The <kbd>tutorial_keys.txt</kbd> file will show you the top key words in each topic. Each paragraph will correspond to a topic and all words in a paragraph will belong to that topic. It is up to you to look through these words and decide what the topic may have been about. This is where your humanistic inquiry brain should come in.</li><br>
			<li>The third file, tutorial_keys.txt is a text file that indicate the breakdown, by percentage, of each topic within each original text file you imported.</li><br>
			<li><em>All of these files should now be in your main <kbd>mallet</kbd> directory.</em></li><br>
		</ul>
	</li>
</ul>


<h2>You Have Produced an Output, What Now?</h2>
<ul>
	<li>At this point, it is recommended that you import the contents of your <kbd>tutorial_composition.txt</kbd> file into a spread sheet. The first column will have a file number, the second will have the name of that file, and every subsequent column will have the proportion of a given topic present in that file. Column C will respond to topic 0, column D to topic 1, and so forth. All the numbers in a given row will add up to 1. Each subsequent row will be the same for each succeeding file in the folder you imported into mallet.</li><br>
	<li>This file was created to be a useful distillation of <a href="https://programminghistorian.org/en/lessons/topic-modeling-and-mallet#your-first-topic-model">this</a> tutorial for those working on the landtalk project wishing to create a topic model for the conversations from the Land Talk site. More information and details can be found there. I recommend also looking through the possible command flags and thinking carefully about which, if any, parameters to tweak. </li>
</ul>
</html>

