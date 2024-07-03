import os
from textSummarizer.logging import logger
from transformers import AutoTokenizer
from datasets import load_dataset, load_from_disk
from textSummarizer.entity import DataTransformationConfig




class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config #assigning configurations here
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name) #tokenizer name from where we want to tokenize
        #autotokenizer loads pre-trained tokenizer, It does:
        #Splitting text into individual words or sub-word units (tokens).
        #Mapping these tokens to unique integer IDs the model can understand.
        #Adding special tokens (e.g., padding tokens) for specific tasks.
    

    
    def convert_examples_to_features(self,example_batch):#taking batch of examples from input
        input_encodings = self.tokenizer(example_batch['dialogue'] , max_length = 1024, truncation = True )
        #taking 'dialogue' text from example batch, max length of encoded text is 1024
        # truncation=True indicates that if the dialogue exceeds 1024 tokens, it will be truncated (cut off) to fit the limit.
        
        with self.tokenizer.as_target_tokenizer():
            target_encodings = self.tokenizer(example_batch['summary'], max_length = 128, truncation = True )
            
        return {
            'input_ids' : input_encodings['input_ids'],# The list of integer IDs representing the encoded dialogue tokens.
            'attention_mask': input_encodings['attention_mask'], # binary mask indicating which parts of the dialogue are relevant (1) and which can be ignored (0) by the model (useful for padding)
            'labels': target_encodings['input_ids'] #The list of integer IDs representing the encoded summary tokens (treated as labels for training)
        }
    

    def convert(self):
        dataset_samsum = load_from_disk(self.config.data_path) #here we are loading the samsum dataset from disk
        #samsum dataset has 3 columns: "id", "dialogue", "summary" in apache arrow format
        dataset_samsum_pt = dataset_samsum.map(self.convert_examples_to_features, batched = True)#map the above function to each 
        #batch of the dataset as here we have kept batched = True
        dataset_samsum_pt.save_to_disk(os.path.join(self.config.root_dir,"samsum_dataset")) #saving the data after transformation on the disk