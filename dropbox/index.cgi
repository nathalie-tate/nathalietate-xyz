#!/usr/bin/perl
use strict;
use warnings;

my @links = <"dropbox/*">;

my $html = qq{<form action="process.cgi" method="GET">};

for (@links)
{
  $html .= qq{<input type="checkbox" name="$_" value='1'><a href='$_' download>$_</a><br/>};
}

$html .= qq{
  <div class="disclaimer">
    <input name="password" type="password" required> <input type="submit" value="Delete"> 
  </div>
</form>};

HTMLdisp($html); 

###############################################################################
sub HTMLdisp                                                                     
{                                                                                
  print "Content-type:text/html\n\n";                                            
  print "<!DOCTYPE html>";
  print "<html>";                                                                
  print "<head>";                                                                
  print "<title>Dropbox</title>";                                                 
  print "<meta charset='utf-8'>";
  print "<LINK href='/style.css' rel='stylesheet' type='text/css'>";
  print "</head>";                                                               
  print "<body>";                                                                
                                                                                 
  foreach(@_)                                                                    
  {                                                                              
    print $_;                                                                    
  }                                                                              
                                                                                 
  print "</body>";                                                               
  print "</html>";                                                               
}
