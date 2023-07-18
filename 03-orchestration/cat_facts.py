import httpx
from prefect import flow, task


# Task tries to fetch data from an API, with max_retries = 4, delay between attempts = 0.1s, and logging. 
@task(retries=4, retry_delay_seconds=0.1, log_prints=True)
def fetch_cat_fact():
    cat_fact = httpx.get("https://f3-vyx5c2hfpq-ue.a.run.app/")
    #An endpoint that is designed to fail sporadically
    if cat_fact.status_code >= 400:
        raise Exception()
    print(cat_fact.text)

# The flow here will trigger the "task" - above. 
@flow
def fetch():
    fetch_cat_fact()


if __name__ == "__main__":
    fetch()