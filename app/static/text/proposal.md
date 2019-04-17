<small>
CSE 6242 - Project Proposal - Georgia Institute of Technology, OMS Analytics<br>

Team 42: Cory Jez, Kyle VanderBush, Alex Furrier, Greg Romrell<br>

February 2019
</small>


# <span class='display-1'>_QBViz_</span>
<br>
<span class = "blockquote"> A modern framework for evaluating Quarterback decision-making and relative performance</span>

----


### Overview and Objective

In the world of professional football, players are evaluated based on individual performance metrics, such as completion percentage and yards per attempt. We believe that there is an opportunity to improve the overall measurement of players (particularly quarterbacks) by quantifying their decisions. Recently, the NFL implemented on-field player-tracking systems, which record the locations and actions of all players on the field. With this data, we believe it is possible to identify and quantify the decisions made by quarterbacks during a game.

### Problem Definition

We plan to take an opportunity-cost approach to measuring quarterback decision-making and thusly, performance above expectation, by using machine learning techniques applied to NFL player-tracking data. Our model will produce a logistic catch-probability model, and leveraging that to provide an expected value of outcomes of each play, we will then measure results against actual quarterback outcomes to identify most efficient quarterbacks in the NFL.

### Current Practices vs. Our Approach

Simple metrics which are commonplace today, such as _Yards per Attempt_ lack the ability to capture to context of an individual play. This is why current advanced metrics look to leverage that context with objective functions such as expected win-probability added (Goldner). The NFL themselves has also distributed many new metrics through their use of [Next Gen Stats](http://www.nfl.com/news/story/0ap3000000964655/article/next-gen-stats-introduction-to-completion-probability), however they have not leveraged this idea of completion probabilities to grade quarterbacks in terms of opportunity-costs and decision making.

The next frontier is evaluating the derivative of this function: what are the individual actions inside a play that increase the end-game outcomes the most? Our analysis will investigate this new area with a novel approach of analyzing quarterback play-making at the exact moment of decision, taking into account play context. This will be successful because similar analyses in more dynamic sports like basketball (Cervone) have found great success and wide-adoption.

### Why is this important and what are the future impacts?

The most obvious use-cases are: 1. Analysis of quarterback performance when negotiating contracts, which could be leveraged by coaches, analysts, and general managers. 2. Application in the commercial markets (i.e. gambling, fantasy sports). 3. Discovering situations where the quarterback make suboptimal decisions and decision new game strategies to address it. If our model is successful it will be the only tool of it's kind available in the market today.

### Risks and Payoffs

The biggest risk posed to the group is that our models produce information which is leveraged for decision-making without insight into all possible variables. We are limited by the data provided by the NFL, and therefore we may not be able to model features which may impact quarterback decision-making and performance. This would lead to a framework which lead to decisions based on false-positives. Conversely, if successful, we will have one of the most-accurate and substantial evaluation tools of quarterbacks on the market today

### Cost and Timeline

#### Cost
In terms of monetary costs, the main cost areas will be data storage, compute power and web hosting. Currently the dataset is hosted in AWS under a free tier usage _(estimated storage costs on AWS RDS $20/month)_. As for compute power this is variable and we will start with our own local machines and resources and scale up if necessary. As the dataset is large _(est. 25 GB)_ the processing power required for data cleaning, processing and model training may require additional cloud resources. As for web hosting for a potential web app, we can start with using a free tier Heroku plan and scale up to Hobbyist ($7/month) or Professional ($25+/month) if need be.

#### Timeline

The project can be broken into four main stages, which are outlined below as a timeline. Progress reports represent our "midterm and final" success checks handled by each team member. Thus far the work has been distributed evenly and we anticipate this will continue as each member is assigned an equal task to oversee:

**March 1 - March 8:**



*   Model Building (Cory Jez)

**March 9 - March 15:**



*   Model Building + Progress Check (CJ)
*   Expected Value Analysis (Greg Romrell)

**March 16 - March 22:**



*   Model Building (CJ)
*   Expected Value Analysis (GR)

**March 23 - March 29:**



*   Expected Value Analysis (GR)
*   Web App Construction (Kyle VanderBush)

**March 30 - April 5:**



*   Expected Value Analysis + Progress Check (GR)
*   Web App Construction (KV)

**April 6 - April 12:**



*   Web App Construction + Progress Check (KV)
*   Final Report and Presentation (Alex Furrier)

**April 13 - April 19:**



*   Final Report and Presentation + Progress Check (AF)

### Literature Review

Alamar, B. (2010). **Measuring Risk in NFL Playcalling.**  _Journal of Quantitative Analysis in Sports_


Burke, B. (2010). **[Expected Points (EP) and Expected Points Added (EPA) Explained](http://archive.advancedfootballanalytics.com/2010/01/expected-points-ep-and-expected-points.html).** _Advanced Football Analytics._


Berri, D., Schmidt, M. (2010). **Measuring Wins Produced In Football.** _PH Professional Business._

Goldner, K. (2012). **A Markov Model of Football: Using Stochastic Processes to Model a Football Drive.** _Journal of Quantitative Analysis in Sports_

Lock, D., Nettleton, D. (2014). **Using Random Forests to Estimate Win Probability before each Play of an NFL Game.** _Journal of Quantitative Analysis in Sports._

Pelechrinis, K., Winston, W., Sagarin, J., & Cabot, V. (2018). **Evaluating NFL plays: Expected points adjusted for schedule.** _CEUR_.


Yam, D. , Lopez, M. (2018). **[Quantifying the causal effects of conservative fourth down decision making in the National Football League.](http://archive.advancedfootballanalytics.com/2010/01/expected-points-ep-and-expected-points.html)** _SSRN._



1. The above papers all evaluate play based on a win-probability or expected-score model based on play outcomes.
2. These represent the state of the art, providing us with potential model outcome variables
3. We will incorporate intra-play effects (qb orientation), not just play outcome data (receptions)

----

Cervone, D., D'Amour, A., Bornn, L., & Goldsberry, K. (2014). **POINTWISE: Predicting Points and Valuing Decisions in Real Time with NBA Optical Tracking Data.** _Sloan Analytics Conference._

Burke, B. (2019). **DeepQB: Deep Learning with Player Tracking to Quantify Quarterback Decision-Making & Performance.** _Sloan Sports Analytics Conference _


1. These papers use intra-play tracking data to evaluate player decision making
2. They are the most closely related to our work, thus can provide the most relevant information to draw from.
3. Both papers till use play and game outcome effects, rather than play level outcomes, which we will explore.

-----

Yurko, R., Ventura, S., & Horowitz, M. (2018). **nflWAR: A Reproducible Method for Offensive Player Evaluation in Football.** _ArXiv_.



1. Build a framework that enables wins-above-replacement (WAR) calculations for football.
2. They have similar inputs as us, but a different objective function
3. Focuses on on-off field as their outcome variable, which is not ideal in a low substitution sport like football.

-----

Ganguly, S., Frank, N. (2018). **The Problem with Win Probability Models.** _Sloan Sports Analytics Conference_



1. There are many common shortcomings for win probability models, most notably the lack of context awareness and uncertainty propagation
2.  A key factor of the usefulness of our analysis lies in the ability to quantify the value of a completed catch. This 'value' will ideally be change in win probability.
3. The paper cites contextual awareness as a key shortcoming for models which will require a great deal of feature engineering and domain expertise to integrate.

-----

Skinner, B. (2011). **Scoring Strategies for the Underdog: A general, quantitative method for determining optimal sports strategies.** _ArXiv_.



1. What are the optimal strategies for risk/reward payoff when trailing in various sports
2. Need to quantify the potential gain from difficult, low probability catches
3. Analysis is high level by reducing the passing plays into two types (short and long pass), while we will have more detailed data
