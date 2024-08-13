import requests

def zk_proof_scan(target_url):
    zk_proofs = ["zk-proof-example1", "zk-proof-example2"]
    for proof in zk_proofs:
        response = requests.get(f"{target_url}?proof={proof}")
        if response.status_code == 200:
            print(f"Zero-Knowledge Proof {proof} is supported by {target_url}")