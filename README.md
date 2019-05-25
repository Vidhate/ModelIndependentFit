## Model Independent Fit
The purpose of this repo is to find the most optimum values of a certain vector (which sets the parameters that defines a function) without any knowledge about the expected values of the function.<br>
It can be clearly seen that this problem cannot be trivially solved from methods like Linear Regression, which necessarily needs the function values at gievn inputs, from which the Regression can "learn" and later start predicting.<br>
The tentative methodology currently explored is as follows-
<ol>
  <li>Find the general trends of the function by using a wide range of randomly distributed parameter values in a certain known prior range. Possibly pin down a certain trend and characterize it and use it in the following steps.</li>
  <li>Find trends in the values of parameters which best predict the trend in the function and characterize it.</li>
  <li>Try defining a mean for the function from the above Monte-Carlo like approach. Also define a variance/cost-function, the value of which might float arbitrarily.</li>
  <li>Run a <b>Metropolis-Hastings(MH)</b> algorithm which minimizes the cost function while moving uphill in the parameter space.</li>
  <li>Run multiple ensembles of MH and wuote statistics on the best values of the parameters found.</li>
</ol>
<br><br>

<h2> Code Description </h2>
<ul>
  <li><i>SampleFunction</i> - approach towards finding trends in the function and parameters that define it</li>
  <li><i>DataCleaner</i> - Filter relevant values to be used from a full data dump, drastically reducing the source data size</li>
</ul>
