#!/usr/bin/perl

while(1)
{
	($sec,$min,@_) = localtime(time);
	if($sec == 0 && $min % 6 ==0)
	{
		print "$min\n";
		system("t followers > followers.txt");
		open  FOLLOWERS, "<", "followers.txt" or die;

		@followers = <FOLLOWERS>;


		for $follower(@followers)
		{
			system("t block $follower");
			system("t delete block $follower");
		}
	}
}
