# SimpleAssetTracker

## The Open-Source Asset Tracker for growing Start-Ups

[Task](#Task) | [Contributors](#Contributors) | [Running Locally](#Local) | [Deploying To Heroku](#Deployment) |


### <a name="Task">The Task</a>

Ever struggled keeping track of which Mac Book each of your employees are holding on to? Do you need a way of tracking when an item changes hands with another? Maybe you're struggling to keep on top of when your leases end? Never fear, SimpleAssetTracker is here!

Providing a barebones yet full experience, this app was built with smaller start-ups in mind - where you don't need a load of fancy-shmancy features.


### <a name="Contributors">Contributors</a>

The team over at SimpleAssetTracker consists of:

- [John Baxter](https://github.com/john-baxter)

- [Haydon Houghton](https://github.com/Kefuri)

- [Richard Pattinson](https://github.com/richardpattinson)

- [Dawid Szpener](https://github.com/DawidSzpener)

### <a name="Local">Running Locally</a>
To run this app locally, you'll first need to clone the repository using `git clone <repository-link>`

We use Postgres as our Database software. You'll need to install Postgres too!

To do so on Mac:
`brew install postgres`

To do so on Windows:
You'll want to download an official release from [here](https://www.postgresql.org/download/windows/)

Now that you've done that, we'd advise you to set up an environment for this project. If you don't know how to do that, we can guide you!

### Running tests
To run test it is required you have geckodriver installed. 
Either install it with brew
```
  $ brew install geckodriver
```
Or download latest release from:
```
  https://github.com/mozilla/geckodriver/releases
```

To run tests make sure you are in root directory and put the commnad bellow in your terminal:
```
  $ python manage.py test functional_tests
```

### Deploying To Heroku

In progress.