Summary:	The SquirrelMail, a WebMail package
Summary(pl):	Wiewórcza Poczta, Poczta przez WWW
Name:		squirrelmail
Version:	1.1.2
Release:	1
License:	GPL
Group:		Applications/Mail
Group(pl):	Aplikacje/Poczta
Source0:	squirrelmail-1.1.2.tar.bz2

ExclusiveOS:	Linux
URL:		http://www.squirrelmail.org
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	webserver
Requires:	imapdaemon
Provides:	webmail 
Buildarch:	noarch

%description
This package contains the Squirrelmail, a webmail system which 
allows you check mail by any cookie-aware WWW browser.

%description -l pl
Pakiet zawiera Wiewiórcz±Pocztê, system pozwalaj±cy sprawdzaæ pocztê 
przez dowoln±, obs³uguj±c± ciasteczka przegl±darkê WWW.

%prep 
rm -rf %{buildroot}
%setup -q 

%build
#cp -avR * %{buildroot}

%files 
%defattr(730,http,http,755)
%dir /home/httpd/html/squirrel/data

%install
install -d %{buildroot}/home/httpd/html/squirrel
install -d %{buildroot}/usr/share/docs/squirrel/
install configure index.php %{buildroot}/home/httpd/html/squirrel
install AUTHORS COPYING ChangeLog INSTALL README UPGRADE %{buildroot}/usr/share/docs/squirrel
rm AUTHORS COPYING ChangeLog INSTALL README UPGRADE 
cp -avR * %{buildroot}/home/httpd/html/squirrel
gzip -9nf %{buildroot}/usr/share/docs/squirrel/*
