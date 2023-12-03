from typing import List
import json

# Assuming a simplified LangChainRepo object that might look something like this
lang_chain_repo = {
    'Runnable': [...],  # List of Runnable objects
    'Chain': [...],     # List of Chain objects
    'Pipeline': [...],  # List of Pipeline objects
    'Agent': [...]      # List of Agent objects
}

def tokenize_lang_chain_repo(repo: dict) -> List[str]:
    tokens = []
    
    # Tokenize each Runnable
    for runnable in repo.get('Runnable', []):
        tokens.append(f"RUNNABLE_ID:{runnable['id']}")
        tokens.append(f"RUNNABLE_NAME:{runnable['name']}")
        tokens.extend(f"METADATA_{k}:{v}" for k, v in runnable['metadata'].items())
        tokens.append(f"SOURCE_CODE:{json.dumps(runnable['source_code'])}")

    # Tokenize each Chain
    for chain in repo.get('Chain', []):
        tokens.append(f"CHAIN_ID:{chain['id']}")
        tokens.append(f"CHAIN_NAME:{chain['name']}")
        tokens.extend(f"METADATA_{k}:{v}" for k, v in chain['metadata'].items())
        tokens.append(f"SOURCE_CODE:{json.dumps(chain['source_code'])}")

    # Tokenize each Pipeline
    for pipeline in repo.get('Pipeline', []):
        tokens.append(f"PIPELINE_ID:{pipeline['id']}")
        tokens.append(f"PIPELINE_NAME:{pipeline['name']}")
        tokens.extend(f"METADATA_{k}:{v}" for k, v in pipeline['metadata'].items())
        tokens.append(f"SOURCE_CODE:{json.dumps(pipeline['source_code'])}")

    # Tokenize each Agent
    for agent in repo.get('Agent', []):
        tokens.append(f"AGENT_ID:{agent['id']}")
        tokens.append(f"AGENT_NAME:{agent['name']}")
        tokens.extend(f"METADATA_{k}:{v}" for k, v in agent['metadata'].items())
        tokens.append(f"SOURCE_CODE:{json.dumps(agent['source_code'])}")
    
    return tokens

# Example usage
tokens = tokenize_lang_chain_repo(lang_chain_repo)
print(tokens)
