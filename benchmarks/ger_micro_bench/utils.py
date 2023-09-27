import datasets
import random

def process_docs(dataset: datasets.Dataset):
    def _helper(doc):
      # modifies the contents of a single
      # document in our dataset.
      
      possible_answers=['A', 'B', 'C', 'D', 'E']

      random.shuffle(possible_answers)
      distractor_no=0
      while possible_answers:
        distractor = possible_answers.pop(0)
        if distractor == doc["output"]:
          continue
        else:
           distractor_no+=1
           doc['distractor'+str(distractor_no)] = distractor
      assert distractor_no == 4
      return doc
    return dataset.map(_helper) # returns back a datasets.Dataset object