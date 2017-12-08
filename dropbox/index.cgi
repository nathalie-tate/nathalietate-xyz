#!/usr/bin/perl
use strict;
use warnings;

my @links = <"dropbox/*">;

my $html = qq{<form action="" method="POST">};

for (@links)
{
  $html .= qq{<input type="checkbox" /> <a href='$_' download>$_</a><br/>};
}

$html .= qq{<input type="password">\n<input type = "submit"> </form>};

HTMLdisp(@links); 

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
