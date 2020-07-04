package nathalietate::xyz;
use strict;
use warnings;
use Dancer2;

our $VERSION = '0.1';

get '/' => sub 
{
  template 'index' => 
  { 
    'title' => 'Nathalie Tate',
    'copy' => getCopy()
  };
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

sub getCopy
{
  my @phrases = 
  (
    "Strange but not a stranger",
    "Decay exists as an extant form of life",
    "Beyond the Flesh and the Real",
    "You cannot kill me in a way that matters"
  );


  return $phrases[ rand @phrases ];
}

true;
