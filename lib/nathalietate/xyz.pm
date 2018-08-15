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

get '/contact' => sub
{
  template 'contact' => { 'title' => 'Contact' };
};

get '/projects' => sub
{
  template 'projects' => { 'title' => 'Projects' };
};

get '/writing' => sub
{
  template 'writing' => { 'title' => 'Writing' }; 
};

true;
