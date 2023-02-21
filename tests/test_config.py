from cf_pages_delete_previews import config

def test_redact():

    secretData = {
        "api_key":"A_REALLY_BIG_SECRET",
        "headers":{"apiKey":"A_REALLY_BIG_SECRET"},
        "accountID":"12345",
        "everythingElse":"Some Non Secret Stuff"
    }
    assert config.redact(secretData).get("api_key")=='<REDACTED>'
    assert not config.redact(secretData).get("headers")
