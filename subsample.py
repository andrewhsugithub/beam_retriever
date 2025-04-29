import json
import os


sampled_path = './results/downstream_llm/example_hotpot_open_source.jsonl'
sampled_data = open(sampled_path).readlines()
sampled_data = [json.loads(line) for line in sampled_data]
sampled_ids = []
for data in sampled_data:
    sampled_ids.append(data['id'])

path = './datasets/mrc/hotpotqa/hotpot_dev_distractor_v1.json'
dev_data = json.load(open(path, 'r'))
ids = []
documents = []
for idx, data in enumerate(dev_data):
    if data['_id'] not in sampled_ids:
        continue
    data['question_id'] = data.pop('_id')
    ids.append(data['question_id'])
    documents.append(data)


output_path = './processed_data/hotpotqa/test_subsampled.jsonl'
os.makedirs(os.path.dirname(output_path), exist_ok=True)

NUM_SAMPLE_DOCS = 5

with open(output_path, 'w') as f:
    for document in documents[:NUM_SAMPLE_DOCS]:
        f.write(json.dumps(document) + '\n')