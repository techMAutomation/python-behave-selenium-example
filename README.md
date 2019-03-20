NOTE: To run the test navigate to the features' folder in the terminal

i)  To Run all the Feature files:
        behave

ii) To Run Single Feature File:
        behave login.feature

iii)To Run a specific Scenario:

- Tag the scenario with any Tag name, For ex: @wip
- Next, run the following command:  behave login.feature --tags=wip

    --In the result displays list of Un-tagged Scenarios and Tagged Scenarios. To skip the list of Un-Tagged scenarios display, need to run the command as follows:
        behave login.feature --no-skipped --tags=wip

Link: https://behave.readthedocs.io/en/latest/behave.html


