#!/usr/bin/python
import MySQLdb as mdb
import sys
import cgi
import cgitb
import datetime
from get_price import get_price 


print "Content-type: text/html\n\n";
print """
<html><head>
<title>KaratCalc.com - Take the guesswork out of Gold Pricing</title>
<script src='http://code.jquery.com/jquery-latest.js'></script>
<script src='http://www.karatcalc.com/kalc.js'></script>
<style ="text/css">
#container {
width: 80%;
margin: 10px auto;
background-color: #fff;
color: #333;
border: 1px solid gray;
line-height: 130%;
}
#ct_toggle {
width:31%;
height:20px;
}
#calctable {
top:20px;
width: 50%;
}
#SHeader {
padding: .5em;
background-color: #ddd;
border-bottom: 1px solid gray;
}
#footer {
margin: 10px auto;
width: 50%;
font-size:12px;
}
.calc {
font-size:12px;
}
#about {
width:60%;
height:20%;
position:absolute;
top:20%;
left:40%;
opacity:100;
}
</style>

</head><body>
"""

form = cgi.FieldStorage()
weight="grams"
wt=0
wt1="gram"
if ("weight" in form): 
	weight=form["weight"].value
Ten="10"
if ("Ten" in form): 
	Ten=form["Ten"].value
Fourteen="10"
if ("Fourteen" in form): 
	Fourteen=form["Fourteen"].value
Eighteen="10"
if ("Eighteen" in form): 
	Eighteen=form["Eighteen"].value
Twentytwo="10"
if ("Twentytwo" in form): 
	Twentytwo=form["Twentytwo"].value
Pr_toz=""
if ("Pr_toz" in form): 
	Pr_toz=form["Pr_toz"].value

(Pr_toz,upd_time)=get_price("usd")
upd_time=(datetime.datetime.fromtimestamp(upd_time).strftime('%m-%d-%Y %H:%M:%S'))
#Pr_toz=1625.00
Pr_gram=round(Pr_toz/31.1,2)
Pr_oz=round(Pr_toz/1.09714286,2)
print '<script type="text/javascript">'
print 'var Pr_gram=%.02f' % (Pr_gram)
print 'var Pr_oz=%.02f' % (Pr_oz)
print '</script>'
print """
<div id="container">
<div id="SHeader">Step 1: Determine what type of gold you have:
<a href="http://www.wikihow.com/Tell-if-Gold-Is-Real" target="_blank">6 steps to test gold</a>
&nbsp;<a href="http://www.amazon.com/PuriTEST-Ultimate-Testing-Magnifying-Reference/dp/B005JU83PA" target="_blank">Gold Karat Testing Kit</a>
<br /></div>
<div id="SHeader">Step 2: Weight each Karat classification, grams or ounces</div>
<div id="SHeader">Step 3 - Enter weight for each karat type below</div>
<div class="calctable" id="calctable">
"""
print'<span title="Last updated: %s">Current Price of gold is $%.2f per Troy Ounce</span>' %(upd_time,Pr_toz)
print '<button id="hide">Toggle Price Calc</button>'


Types={"Ten":"0.4167","Fourteen":".5833","Eighteen":"0.750","Twentytwo":".9167"}
print '<table border=1>'
print '<TR>'
print '<TD>How much of each<br/> do you have? </TD>'
print '<TD align=right>'
if weight=="grams":
 wt=Pr_gram
 wt1="gram"
 print '<input type="radio" name="weight" id="weight" value="grams" checked />Grams'
 print '<input type="radio" name="weight" id="weight" value="ounces" />Ounces<br />'
elif weight=="ounces":
 wt=Pr_oz
 wt1="oz"
 print '<input type="radio" name="weight" id="weight" value="grams" />Grams'
 print '<input type="radio" name="weight" id="weight" value="ounces" checked />Ounces'
print '</TD><TD class="calc">&nbsp;</TD>'
print '<TD>Markdown %<select id="markdown" name="markdown">'
per=[100,90,80,70,60,50,40,30,20,10]
for x in per:
 print '<option value=%2s>%2s</option>' %(x,x)
print'</select></TD>'
print '<TR><TD align=right>10k</TD>'
print '<TD><input type=text name="Ten" id="Ten" value="'+Ten+'" /></TD>'
print '<TD class="calc" id="calc_10">10k=%3s %2s * $%.2f/%4s * %s</TD>' %(Ten,weight,wt,wt1,Types["Ten"])
print '<TD><div class="Ten_dol">$'+str(round(float(Ten)*wt*float(Types["Ten"]),2))+'</div></TD></TR>'

print '<TR><TD align=right>14k</TD>'
print '<TD><input type=text name="Fourteen" id="Fourteen" value="'+Fourteen+'" /></TD>'
print '<TD class="calc" id="calc_14">14k=%3s %2s * $%.2f/%4s * %s</TD>' %(Fourteen,weight,wt,wt1,Types["Fourteen"])
print '<TD><div class="Fourteen_dol">$'+str(round(float(Fourteen)*wt*float(Types["Fourteen"]),2))+'</div></TD></TR>'

print '<TR><TD align=right>18k</TD>'
print '<TD><input type=text name="Eighteen" id="Eighteen" value="'+Eighteen+'" /></TD>'
print '<TD class="calc" id="calc_18">18k=%3s %2s * $%.2f/%4s * %s</TD>' %(Eighteen,weight,wt,wt1,Types["Eighteen"])
print '<TD><div class="Eighteen_dol">$'+str(round(float(Eighteen)*wt*float(Types["Eighteen"]),2))+'</div></TD></TR>'

print '<TR><TD align=right>22k</TD>'
print '<TD><input type=text name="Twentytwo" id="Twentytwo" value="'+Twentytwo+'" /></TD>'
print '<TD class="calc" id="calc_22">22k=%3s %2s * $%.2f/%4s * %s</TD>' %(Twentytwo,weight,wt,wt1,Types["Twentytwo"])
print '<TD><div class="Twentytwo_dol">$'+str(round(float(Twentytwo)*wt*float(Types["Twentytwo"]),2))+'</div></TD></TR>\n'
print '<TR><TD> </TD><TD class="tgold">Weight Total</TD><TD class="calc">&nbsp;</TD><TD class="tdol">$ Total</TD></TR>\n'
print '</TABLE>'
#print '<input type=submit>'
print "</div> <!-- calctable div -->"
print """
<div id="SHeader">Knowing a) What type(s) of gold and b) How much of each type you have will go a long way.  You can haggle price while having a general idea of what to expect from the salesman.<br/>
Use the Markdown menu to display lower price totals. Do not expect full price in return, but do not give in to 30% market value either.
</div>
</div> <!-- container div -->
<div id="about">
About
</div>
<div id="footer">
<a href="mailto:contact@karatcalc.com">Contact</a> || 
Gold prices pulled twice hourly from <a href="http://www.xmlcharts.com/cache/precious-metals.xml" target="_blank">http://www.xmlcharts.com/</a> ||
<a id="abt" class="about">About</a>
</div>

<script type="text/javascript"><!--
google_ad_client = "ca-pub-8472342822434198";
/* Karatcalc */
google_ad_slot = "0952459603";
google_ad_width = 728;
google_ad_height = 90;
//-->
</script>
<script type="text/javascript"
src="http://pagead2.googlesyndication.com/pagead/show_ads.js">
</script>
<script>
$("#hide").click(function () { $(".calc").toggle(); });
$("#abt").click(function () {
 $("#about").toggle();
 $("#container").toggle();
 });

$("#markdown").change(function () {
kalc(10);
kalc(14);
kalc(18);
kalc(22);
});
$("#Ten").change(function () { kalc(10)});
$("#Fourteen").change(function () { kalc(14)});
$("#Eighteen").change(function () { kalc(18)});
$("#Twentytwo").change(function () { kalc(22)});

$(document).ready(function(){
 $(".calc").hide();
 $("#about").hide();
});

$("input[name='weight']").change(function(){
if ($("input[name='weight']:checked").val() == 'grams')  {
  Tg=Pr_gram
}else{
  Tg=Pr_oz
}
  kalc(10);
  kalc(14);
  kalc(18);
  kalc(22);
});
</script>
</body></html>
"""
