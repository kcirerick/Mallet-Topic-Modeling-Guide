rm -R all-out
mkdir all-out
mkdir all-out/conversationResults
python ./python-stuff/load_conversation_files.py
bin/mallet import-dir --input all-out/conversationResults --output all-out/mytrans.mallet --keep-sequence --stoplist-file stoplists/all-stops.txt
for i in 1
do
KEYS="topic_keys_$i.txt"
STATE="topic_state_$i.gz"
COMP="transcript_composition_$i.txt"
bin/mallet train-topics --input all-out/mytrans.mallet --num-topics 50 --output-state all-out/$STATE --output-topic-keys all-out/$KEYS --output-doc-topics all-out/$COMP --random-seed 1
done
python ./python-stuff/load_composition_files.py

