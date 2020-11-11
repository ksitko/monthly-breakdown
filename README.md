# Monthly Break Down Query

Goal: Create a single query which will return a per month breakdown of successful and failed events for the entire month as well as a per user break down. Desired effect would look like so:

```json
{
	"month": "2020-11-01 00:00:00",
	"completed": 3,
	"failed": 2,
	"user": [
		{
			"pk": "1",
			"completed": 2,
			"failed": 0
		},
		{
			"pk": "2",
			"completed": 1,
			"failed": 2
		}
	]
}
```

## Setup

Open your terminal in the repo and copy and paste:

```
python3 -m venv venv;
source venv/bin/activate;
pip install -r requirements.txt;
cd src;
./manage.py migrate;
```

## Running
Run `./manage.py test` inside of the `src/` folder after setting up.

The query along with all the dummy data you need is located in `src/history/tests.py`.
