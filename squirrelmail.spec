Summary:	The SquirrelMail, a WebMail package
Summary(pl):	Wiewórcza Poczta, Poczta przez WWW
Name:		squirrelmail
Version:	1.1.2
Release:	3
License:	GPL
Group:		Applications/Mail
Group(de):	Applikationen/Post
Group(pl):	Aplikacje/Poczta
Group(pt):	Aplicações/Correio Eletrônico
Source0:	http://prdownloads.sourceforge.net/squirrelmail/%{name}-%{version}.tar.bz2
Source1:	squirrelmail-%{version}-config-pl
Source2:	squirrelmail-%{version}-default-user-pl
URL:		http://www.squirrelmail.org/
Requires:	webserver
Requires:	imapdaemon
Provides:	webmail 
Buildarch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the Squirrelmail, a webmail system which allows
you check mail by any cookie-aware WWW browser. Squirrel supports many languages: Polish, Russian, German:

%description -l pl
Pakiet zawiera Wiewiórcz±Pocztê, system pozwalaj±cy sprawdzaæ pocztê
przez dowoln±, obs³uguj±c± ciasteczka przegl±darkê WWW.

%prep 
%setup -q 

%build
echo "No build necessary"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/home/httpd/html/squirrel \
	$RPM_BUILD_ROOT%{_datadir}/docs/squirrel/

install -d $RPM_BUILD_ROOT/home/httpd/html/squirrel/config
install -d $RPM_BUILD_ROOT/home/httpd/html/squirrel/data
install AUTHORS COPYING ChangeLog INSTALL README UPGRADE $RPM_BUILD_ROOT%{_datadir}/docs/squirrel
install doc/* $RPM_BUILD_ROOT%{_datadir}/docs/squirrel
install %{SOURCE1} $RPM_BUILD_ROOT/home/httpd/html/squirrel/config/config.php
install %{SOURCE2} $RPM_BUILD_ROOT/home/httpd/html/squirrel/data/

rm AUTHORS ChangeLog INSTALL README UPGRADE doc/*
cp -avR * $RPM_BUILD_ROOT/home/httpd/html/squirrel

gzip -9nf $RPM_BUILD_ROOT%{_datadir}/docs/squirrel/*

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%doc %{_datadir}/docs/squirrel/*.gz
%defattr(755,http,http,755)
%attr(730,http,http) /home/httpd/html/squirrel/data/
/home/httpd/html/squirrel/index.php
/home/httpd/html/squirrel/configure
/home/httpd/html/squirrel/config/*
/home/httpd/html/squirrel/functions/*
/home/httpd/html/squirrel/help/index.php
/home/httpd/html/squirrel/help/ca/*
/home/httpd/html/squirrel/help/cs/*
/home/httpd/html/squirrel/help/en/*
/home/httpd/html/squirrel/help/fi/*
/home/httpd/html/squirrel/help/fr/*
/home/httpd/html/squirrel/help/it/*
/home/httpd/html/squirrel/help/ko/*
/home/httpd/html/squirrel/help/pl/*
/home/httpd/html/squirrel/help/ru/*
/home/httpd/html/squirrel/help/sv/*
/home/httpd/html/squirrel/images/*
#FixMe: do sth with plugins !!!
/home/httpd/html/squirrel/plugins/*
/home/httpd/html/squirrel/po/*
/home/httpd/html/squirrel/src/*
/home/httpd/html/squirrel/themes/*
/home/httpd/html/squirrel/locale/ca/LC_MESSAGES/squirrelmail.mo
/home/httpd/html/squirrel/locale/ca/LC_MESSAGES/squirrelmail.po
/home/httpd/html/squirrel/locale/da/LC_MESSAGES/squirrelmail.mo
/home/httpd/html/squirrel/locale/da/LC_MESSAGES/squirrelmail.po
/home/httpd/html/squirrel/locale/de/LC_MESSAGES/squirrelmail.mo
/home/httpd/html/squirrel/locale/de/LC_MESSAGES/squirrelmail.po
/home/httpd/html/squirrel/locale/cs/LC_MESSAGES/squirrelmail.mo
/home/httpd/html/squirrel/locale/cs/LC_MESSAGES/squirrelmail.po
/home/httpd/html/squirrel/locale/es/LC_MESSAGES/squirrelmail.mo
/home/httpd/html/squirrel/locale/es/LC_MESSAGES/squirrelmail.po
/home/httpd/html/squirrel/locale/fi/LC_MESSAGES/squirrelmail.mo
/home/httpd/html/squirrel/locale/fi/LC_MESSAGES/squirrelmail.po
/home/httpd/html/squirrel/locale/fr/LC_MESSAGES/squirrelmail.mo
/home/httpd/html/squirrel/locale/fr/LC_MESSAGES/squirrelmail.po
/home/httpd/html/squirrel/locale/hr/LC_MESSAGES/squirrelmail.mo
/home/httpd/html/squirrel/locale/hr/LC_MESSAGES/squirrelmail.po
/home/httpd/html/squirrel/locale/hu/LC_MESSAGES/squirrelmail.mo
/home/httpd/html/squirrel/locale/hu/LC_MESSAGES/squirrelmail.po
/home/httpd/html/squirrel/locale/is/LC_MESSAGES/squirrelmail.mo
/home/httpd/html/squirrel/locale/is/LC_MESSAGES/squirrelmail.po
/home/httpd/html/squirrel/locale/it/LC_MESSAGES/squirrelmail.mo
/home/httpd/html/squirrel/locale/it/LC_MESSAGES/squirrelmail.po
/home/httpd/html/squirrel/locale/ko/LC_MESSAGES/squirrelmail.mo
/home/httpd/html/squirrel/locale/ko/LC_MESSAGES/squirrelmail.po
/home/httpd/html/squirrel/locale/nl/LC_MESSAGES/squirrelmail.mo
/home/httpd/html/squirrel/locale/nl/LC_MESSAGES/squirrelmail.po
/home/httpd/html/squirrel/locale/no/LC_MESSAGES/squirrelmail.mo
/home/httpd/html/squirrel/locale/no/LC_MESSAGES/squirrelmail.po
/home/httpd/html/squirrel/locale/pl/LC_MESSAGES/squirrelmail.mo
/home/httpd/html/squirrel/locale/pl/LC_MESSAGES/squirrelmail.po
/home/httpd/html/squirrel/locale/ru/LC_MESSAGES/squirrelmail.mo
/home/httpd/html/squirrel/locale/ru/LC_MESSAGES/squirrelmail.po
/home/httpd/html/squirrel/locale/sr/LC_MESSAGES/squirrelmail.mo
/home/httpd/html/squirrel/locale/sr/LC_MESSAGES/squirrelmail.po
/home/httpd/html/squirrel/locale/sv/LC_MESSAGES/squirrelmail.mo
/home/httpd/html/squirrel/locale/sv/LC_MESSAGES/squirrelmail.po
/home/httpd/html/squirrel/locale/tw/LC_MESSAGES/squirrelmail.mo
/home/httpd/html/squirrel/locale/tw/LC_MESSAGES/squirrelmail.po
/home/httpd/html/squirrel/locale/pt_BR/LC_MESSAGES/squirrelmail.mo
/home/httpd/html/squirrel/locale/pt_BR/LC_MESSAGES/squirrelmail.po
/home/httpd/html/squirrel/locale/index.php
/home/httpd/html/squirrel/locale/no_NO_ny/LC_MESSAGES/squirrelmail.mo
/home/httpd/html/squirrel/locale/no_NO_ny/LC_MESSAGES/squirrelmail.po
