# workpathapi

This package allows you to interact with the [Workpath](https://www.workpath.com/) [API](https://developer.workpath.com/).

## Prerequisites

There is only one mandatory Python package that needs to be installed to use `workpath` i. e. `requests`. One can install it with the following command.

```
pip install requests
```

If you want the API to return a pandas DataFrame you additionally need to install pandas.

```
pip install pandas
```

## Installation

If all prerequisites are met the installation is as simple as executing the command
```
pip install workpath
```

## Usage

To get data from the Workpath API you only need three steps.

### 1. Import module

Import the module, for example like this.

```
from workpathapi import WorkpathAPI
```

### 2. Instanciate WorkpathAPI

Create an instance of the WorkpathAPI.

```
api = WorkpathAPI(company='dataatelier', api_token='YOUR_WORKPATH_TOKEN')
```

You need to pass two arguments. Your company and the API token. 
Note: If your API token is set as an environment variable as `WORKPATH_API_TOKEN = "YOUR_WORKPATH_TOKEN"` then you don't have to pass the argument `api_token`.

### 3. Get goals from the API

If you want to get all goals, simply execute

```
goals = api.get_goals()
```

The output corresponds to the output of API endpoint `goals`, described [here](https://developer.workpath.com/#get-goals)
If you want the result as a pandas DataFrame you can pass the argument `output_format='DataFrame'`


If you want information about a specific goal, one can execute

```
goal = api.get_goal(goal_id=1001)
```

See API [documentation](https://developer.workpath.com/#get-goal-details) for further information.
