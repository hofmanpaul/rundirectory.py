*Open the data and do a DID Analysis and a difference in means

*ssc install estout 

cd "$GITLOC/rundirectory.py"

import delimited using "01_Data/02_Clean/appended.csv", clear

gen treat_time=treat*time

eststo clear
eststo: reg income treat time treat_time

eststo: reg income treat if time==2

esttab  using "02_Output/results.tex", replace star( * 0.10 ** 0.05 *** 0.01) b(3) se label  fragment ///
	mlabels("Income DiD" "Income difference mean")
