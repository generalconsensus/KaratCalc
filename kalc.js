function kalc (kar) {
 if ($("input[name='weight']:checked").val() == 'grams') {
  wt=Pr_gram;
  typ="gram";
  typs="grams";
 }else {
  wt=Pr_oz;
  typ="ounce";
  typs="ounces";
}
 var myweight = .00001;
 var karat = 0.0001;
 var mark = $("#markdown").val();
 var per = mark/100;
  w10 = new Number($("#Ten").val());
  k10 = 0.4167;
  x10 = Math.round(w10*wt*k10*per*100)/100;
  w14 = new Number($("#Fourteen").val());
  k14 = 0.5833;
  x14 = Math.round(w14*wt*k14*per*100)/100;
  w18 = new Number($("#Eighteen").val());
  k18 = 0.7500;
  x18 = Math.round(w18*wt*k18*per*100)/100;
  w22 = new Number($("#Twentytwo").val());
  k22 = 0.9167;
  x22 = Math.round(w22*wt*k22*per*100)/100;
 switch (kar)
 {
 case 10:
  if ($("#Ten").val()==1) { typs=typ; }
  x="10k: "+$("#Ten").val()+" "+typs+" * $"+wt+"/"+typ+" * 0.4167";
  $("#calc_10").html(x);
  $(".Ten_dol").html("$"+x10);
  break;
 case 14:
  if ($("#Fourteen").val()==1) { typs=typ; }
  x="14k: "+$("#Fourteen").val()+" "+typs+" * $"+wt+"/"+typ+" * 0.5833";
  $("#calc_14").html(x);
  $(".Fourteen_dol").html("$"+x14);
  break;
 case 18:
  if ($("#Eighteen").val()==1) { typs=typ; }
  x="18k: "+$("#Eighteen").val()+" "+typs+" * $"+wt+"/"+typ+" * 0.750";
  $("#calc_18").html(x);
  $(".Eighteen_dol").html("$"+x18);
  break;
 case 22:
  if ($("#Twentytwo").val()==1) { typs=typ; }
  x="22k: "+$("#Twentytwo").val()+" "+typs+" * $"+wt+"/"+typ+" * 0.9167";
  $("#calc_22").html(x);
  $(".Twentytwo_dol").html("$"+x22);
  break;
 }
  var totg =Math.round(w10+w14+w18+w22);
  var totd =Math.round(x10+x14+x18+x22*100)/100;
 $(".tgold").html(totg+" "+typ);
 $(".tdol").html("$"+totd);

}
