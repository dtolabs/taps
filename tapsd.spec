name: tapsd
version: 1.0
release: 0
summary: Taps Service Daemon 
group: ctier
license: GPL

requires: lighttpd >= 1.4
requires(post): chkconfig
requires(postun): chkconfig

%description
Rundeck supports dynamic input fields using valueUrls.  These urls can be served from the file system using file:// or http:// using a webservice.  This webservice provides a mechanism to serve dynamic options in an easy to use, easy to integration fashion.

The webservice uses the CGI standard to return json to Rundeck.  By placing a file with the *.options under the /var/rundeck directory, any acceptable #! can be used to process the CGI request.

%files
%defattr(644, taps, taps, 755)
%attr(-, ctier, ctier) %config /etc/tapsd/options.conf
%attr(755, -, -) /etc/rc.d/init.d/tapsd
%attr(-, ctier, ctier) %ghost /var/log/tapsd/options-webservice.error.log
%attr(-, ctier, ctier) %ghost /var/log/tapsd/options-webservice.access.log
%attr(-, ctier, ctier) %ghost /var/log/tapsd/dav.access.log
%attr(-, ctier, ctier) %dir /var/run/tapsd/dav
/usr/sbin/tapsd

%post
/sbin/chkconfig --add tapsd

%postun
if [ "$1" = 0 ]; then
	/sbin/chkconfig --del tapsd
fi

%changelog
* Wed Oct 20 2010 Noah Campbell <noah@dtosolutions.com> 1.0
	- Initial spec file.
