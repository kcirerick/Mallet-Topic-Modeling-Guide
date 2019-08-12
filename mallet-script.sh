python ./python-stuff/load-conversation-files.py
bin/mallet import-dir --input python-stuff/conversationResults --output mytrans.mallet --keep-sequence --stoplist-file stoplists/all-stops.txt
for i in 1 2 3 4 5
do
KEYS="topic_keys_$i.txt"
STATE="topic_state_$i.gz"
COMP="transcript_composition_$i.txt"
bin/mallet train-topics --input mytrans.mallet --num-topics 300 --output-state $STATE --output-topic-keys $KEYS --output-doc-topics $COMP
done
