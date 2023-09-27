import datasets
import random

def process_docs(dataset: datasets.Dataset):
    def _helper(doc):
      # modifies the contents of a single
      # document in our dataset.
      
      correct_answer_col='mc_answer'+doc['correct_answer_num']
      doc['correct_answer'] = doc[correct_answer_col]
      
      possible_answer_cols=['mc_answer1', 'mc_answer2', 'mc_answer3', 'mc_answer4']

      random.shuffle(possible_answer_cols)
      distractor_no=0
      while possible_answer_cols:
        distractor_col = possible_answer_cols.pop(0)
        if distractor_col == correct_answer_col:
          continue
        else:
           distractor_no+=1
           doc['distractor'+str(distractor_no)] = doc[distractor_col]
      assert distractor_no == 3
      return doc
    return dataset.map(_helper) # returns back a datasets.Dataset object