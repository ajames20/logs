# Steps to Run?

PreReqs:

Python3
Vagrant
VirtualBox

### Setup Project:

1. Install [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/)
1. Download or Clone [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm) repository.
1. Download the data from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).
1. Unzip after downloading.
1. Copy the newsdata.sql into the vagrant folder inside of the repo you downloaded.

### Steps to Run `logs.py` and view query results

1. Launch the Vagrant VM inside Vagrant sub-directory.

```
~ vagrant up
```

2. SSH into VM.

```
~ vagrant ssh
```

3. Load the data in to local db.

```
~ psql -d news -f newsdata.sql
```

4. Run `logs.py` to view the results of teh queries.

```
~ python3 logs.py
```