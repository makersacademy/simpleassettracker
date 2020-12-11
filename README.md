[![Codeship Status for makersacademy/simpleassettracker](https://app.codeship.com/projects/c56a2e20-a7e4-0138-7d2b-2e8a72535188/status?branch=master)](https://app.codeship.com/projects/402832)
[![codecov](https://codecov.io/gh/makersacademy/simpleassettracker/branch/master/graph/badge.svg?token=XWE9CMYN4K)](https://codecov.io/gh/makersacademy/simpleassettracker)

# SimpleAssetTracker

## The Open-Source Asset Tracker for growing Start-Ups

[Task](#Task) | [Contributors](#Contributors) | [Running Locally](#Local) | [Deploying To Heroku](#Deployment) |


### <a name="Task">The Task</a>

Ever struggled keeping track of which Mac Book each of your employees are holding on to? Do you need a way of tracking when an item changes hands with another? Maybe you're struggling to keep on top of when your leases end? Never fear, SimpleAssetTracker is here!

Providing a barebones yet full experience, this app was built with smaller start-ups in mind - where you don't need a load of fancy-shmancy features.

### The App
![Your Assets](https://user-images.githubusercontent.com/41115973/92376218-29ae4b00-f0fa-11ea-8ce6-c104fb6a44f5.png)

![Add an Asset](https://user-images.githubusercontent.com/41115973/92376522-99bcd100-f0fa-11ea-9999-c300ae07f3d9.png)

![Import Assets](https://user-images.githubusercontent.com/41115973/92376609-bb1dbd00-f0fa-11ea-9d32-a92fd8aaafe2.png)

### <a name="Contributors">Contributors</a>

The team over at SimpleAssetTracker consists of:

- [John Baxter](https://github.com/john-baxter)

- [Catriona Bennett](https://github.com/cmb84scd)

- [Ilias Marios Grigoropoulos](https://github.com/IliasMariosG)

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

#### Using Conda

Anaconda is a useful environment management tool for projects where you don't want to install packages onto your route.

Thankfully, Anaconda provide a great installation guide [here](https://www.anaconda.com/products/individual). Please use the COMMAND LINE installer - we've encountered issues with the graphical one!

Once you've finished the installation, you should be able to navigate over to your terminal and run `conda -V` with no issues.

To create a new environment, run `conda create -n ENV_NAME python=3.8`. This creates a new environment with your name of choice that you can use as a sandbox for python package installation!

You can activate this environment at any time using `conda activate ENV_NAME`

### Installing Packages

There are two different package managers being used for this project - pip and npm.

To install packages for pip, make sure you're in the project root and you are within your environment. Then run `pip install -r requirements.txt` - this will read the requirements file for packages that are needed.

To install node packages, navigate into `/AssetTracker/apps/reactfrontend` and run `npm install`.

### Running tests
To run tests you'll need a version of geckodriver installed. 
Either install it with brew
```
$ brew install geckodriver
```
Or download latest release from:
```
https://github.com/mozilla/geckodriver/releases
```

To run all tests make sure you are in your root directory before running the following:
```
$ python manage.py test AssetTracker.apps
```
To just run the feature (functional) tests then use:
```
$ python manage.py test AssetTracker.apps.functionaltests
```
or for just the unit tests then use:
```
$ python manage.py test AssetTracker.apps.unittests
```
If you are running the tests multiple times then you'll get a database stacktrace. To prevent this you can just add the `--keepdb` flag to the end of the test commands ie
```
$ python manage.py test AssetTracker.apps --keepdb
```
This doesn't affect the running of the tests but does make the ouput much cleaner!

### Deploying To Heroku

Deployment to Heroku can be fast and simple with the proper set-up.
