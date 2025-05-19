# fusion.py

def fusion_match(face_result, fingerprint_result, iris_result):
    """
    Accepts boolean match results from face, fingerprint, and iris modules.
    Returns True if any 2 out of 3 match.
    """
    results = [face_result, fingerprint_result, iris_result]
    return results.count(True) >= 2
