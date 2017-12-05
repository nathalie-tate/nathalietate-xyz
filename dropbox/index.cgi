#!/usr/bin/perl
use strict;
use warnings;

my @links = <"dropbox/*">;

for (@links)
{
  $_ = "<a href='$_' download>$_</a><br/>";
}

HTMLdisp(@links); 

###############################################################################
sub HTMLdisp                                                                     
{                                                                                
  print "Content-type:text/html\n\n";                                            
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
