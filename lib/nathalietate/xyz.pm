package nathalietate::xyz;
use strict;
use warnings;
use Dancer2;

our $VERSION = '0.1';

get '/' => sub 
{
  template 'index' => { 'title' => 'Nathalie Tate' };
};

get '/license' => sub 
{
  template 'license' => { 'title' => 'License' };
};

true;
