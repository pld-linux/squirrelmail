Summary:	The SquirrelMail, a WebMail package
Summary(pl):	Wiewórcza Poczta, Poczta przez WWW
Name:		squirrelmail
Version:	1.1.2
Release:	1
License:	GPL
Group:		Applications/Mail
Group(de):	Applikationen/Post
Group(pl):	Aplikacje/Poczta
Group(pt):	Aplicações/Correio Eletrônico
Source0:	http://prdownloads.sourceforge.net/squirrelmail/%{name}-%{version}.tar.bz2
URL:		http://www.squirrelmail.org/
Requires:	webserver
Requires:	imapdaemon
Provides:	webmail 
Buildarch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the Squirrelmail, a webmail system which allows
you check mail by any cookie-aware WWW browser.

%description -l pl
Pakiet zawiera Wiewiórcz±Pocztê, system pozwalaj±cy sprawdzaæ pocztê
przez dowoln±, obs³uguj±c± ciasteczka przegl±darkê WWW.

%prep 
%setup -q 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/home/httpd/html/squirrel \
	$RPM_BUILD_ROOT%{_datadir}/docs/squirrel/

install configure index.php $RPM_BUILD_ROOT/home/httpd/html/squirrel
install AUTHORS COPYING ChangeLog INSTALL README UPGRADE $RPM_BUILD_ROOT%{_datadir}/docs/squirrel

rm AUTHORS COPYING ChangeLog INSTALL README UPGRADE 
cp -avR * $RPM_BUILD_ROOT/home/httpd/html/squirrel

gzip -9nf $RPM_BUILD_ROOT%{_datadir}/docs/squirrel/*

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(730,http,http,755)
%dir /home/httpd/html/squirrel/data
