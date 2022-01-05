from cf_pages_delete_previews import lib

def test_delete_eligible_true():
    # Test if a eligible, deletable deployment will be marked as such.  
    assert lib.delete_eligible({"name":"1","deploymentID":"1","aliases":None, "environment":"development"}) == True


def test_delete_eligible_false():
    # Test that a production deployment will not be set to eligible.
    assert lib.delete_eligible({"name":"1","deploymentID":"1","aliases":"production","environment":"production"}) == False


def test_delete_eligible_none():
    # Test that junk data will not be set as either true nor false.
    assert lib.delete_eligible({"JunkData":True,"Invalid":"probably"}) == None
