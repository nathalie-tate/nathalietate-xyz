#!/usr/bin/env perl

use strict;
use warnings;
use FindBin;
use lib "$FindBin::Bin/../lib";


# use this block if you don't need middleware, and only have a single target Dancer app to run here
use nathalietate::xyz;

nathalietate::xyz->to_app;

=begin comment
# use this block if you want to include middleware such as Plack::Middleware::Deflater

use nathalietate::xyz;
use Plack::Builder;

builder {
    enable 'Deflater';
    nathalietate::xyz->to_app;
}

=end comment

=cut

=begin comment
# use this block if you want to mount several applications on different path

use nathalietate::xyz;
use nathalietate::xyz_admin;

use Plack::Builder;

builder {
    mount '/'      => nathalietate::xyz->to_app;
    mount '/admin'      => nathalietate::xyz_admin->to_app;
}

=end comment

=cut

