%define	ver	1.2.0
%define rcver	rc2
Summary:	The SquirrelMail, a WebMail package
Summary(pl):	Wiewórcza Poczta, Poczta przez WWW
Name:		squirrelmail
Version:	%{ver}.%{rcver}
Release:	4
License:	GPL
Group:		Applications/Mail
Group(de):	Applikationen/Post
Group(pl):	Aplikacje/Poczta
Group(pt):	Aplicações/Correio Eletrônico
Source0:	http://prdownloads.sf.net/squirrelmail/%{name}-%{ver}-%{rcver}.tar.bz2
Source1:	http://www.squirrelmail.org/plugins/%{name}_plugins-20010604.tar
Patch0:		%{name}-setlocale.patch
URL:		http://www.squirrelmail.org/
Requires:	webserver
Requires:	imapdaemon
Requires:	php
Requires:	php-gettext
Provides:	webmail 
Buildarch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the Squirrelmail, a webmail system which allows
you check mail by any cookie-aware WWW browser. Squirrel supports many
languages: Polish, Russian, German:

%description -l pl
Pakiet zawiera Wiewiórcz±Pocztê, system pozwalaj±cy sprawdzaæ pocztê
przez dowoln±, obs³uguj±c± ciasteczka przegl±darkê WWW.

%prep 
%setup -a1 -q -n %{name}-%{ver}-%{rcver}
%patch0 -p1

# List of usefull plugins (ONLY usefull one should be here)
for i in change_pass*tar.gz username*tar.gz abook_take*tar.gz \
	addgraphics*tar.gz attachment_common*tar.gz vacation*tar.gz \
	squirrelspell*tar.gz sqclock*tar.gz retrieveuserdata*tar.gz \
	quicksave*tar.gz printer_friendly*tar.gz password_forget*tar.gz \
	newmail*tar.gz motd*tar.gz mail_fwd*tar.gz mail_fetch*tar.gz \
	gzip*tar.gz fortune*tar.gz auto_cc*tar.gz; do
		tar xfvz $i -C plugins
done

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/home/httpd/html/squirrel/{config,data} \
	$RPM_BUILD_ROOT%{_datadir}/docs/squirrel/

gzip -9nf AUTHORS ChangeLog INSTALL README UPGRADE doc/*

cp -avR * $RPM_BUILD_ROOT/home/httpd/html/squirrel
cd plugins/squirrelspell
cp sqspell_config.dist sqspell_config.php

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%doc *.gz doc/*.gz
%defattr(755,http,http,755)
%attr(730,http,http) /home/httpd/html/squirrel/data/
/home/httpd/html/squirrel/index.php
/home/httpd/html/squirrel/configure
%config (noreplace) /home/httpd/html/squirrel/config/*
/home/httpd/html/squirrel/functions/*
/home/httpd/html/squirrel/help/index.php
%lang(ca) /home/httpd/html/squirrel/help/ca
%lang(cs) /home/httpd/html/squirrel/help/cs
%lang(en) /home/httpd/html/squirrel/help/en
%lang(fi) /home/httpd/html/squirrel/help/fi
%lang(fr) /home/httpd/html/squirrel/help/fr
%lang(it) /home/httpd/html/squirrel/help/it
%lang(ko) /home/httpd/html/squirrel/help/ko
%lang(pl) /home/httpd/html/squirrel/help/pl
%lang(ru) /home/httpd/html/squirrel/help/ru
%lang(sv) /home/httpd/html/squirrel/help/sv
/home/httpd/html/squirrel/images
/home/httpd/html/squirrel/plugins
/home/httpd/html/squirrel/src
/home/httpd/html/squirrel/themes
/home/httpd/html/squirrel/locale/index.php
%dir /home/httpd/html/squirrel/locale
%dir /home/httpd/html/squirrel/locale/[^i]*
%lang(is) %dir /home/httpd/html/squirrel/locale/is/LC_MESSAGES
%lang(it) %dir /home/httpd/html/squirrel/locale/it/LC_MESSAGES
%lang(ca) /home/httpd/html/squirrel/locale/ca/LC_MESSAGES/squirrelmail.mo
%lang(da) /home/httpd/html/squirrel/locale/da/LC_MESSAGES/squirrelmail.mo
%lang(de) /home/httpd/html/squirrel/locale/de/LC_MESSAGES/squirrelmail.mo
%lang(cs) /home/httpd/html/squirrel/locale/cs/LC_MESSAGES/squirrelmail.mo
%lang(es) /home/httpd/html/squirrel/locale/es/LC_MESSAGES/squirrelmail.mo
%lang(fi) /home/httpd/html/squirrel/locale/fi/LC_MESSAGES/squirrelmail.mo
%lang(fr) /home/httpd/html/squirrel/locale/fr/LC_MESSAGES/squirrelmail.mo
%lang(hr) /home/httpd/html/squirrel/locale/hr/LC_MESSAGES/squirrelmail.mo
%lang(hu) /home/httpd/html/squirrel/locale/hu/LC_MESSAGES/squirrelmail.mo
%lang(is) /home/httpd/html/squirrel/locale/is/LC_MESSAGES/squirrelmail.mo
%lang(it) /home/httpd/html/squirrel/locale/it/LC_MESSAGES/squirrelmail.mo
%lang(ko) /home/httpd/html/squirrel/locale/ko/LC_MESSAGES/squirrelmail.mo
%lang(nl) /home/httpd/html/squirrel/locale/nl/LC_MESSAGES/squirrelmail.mo
%lang(no) /home/httpd/html/squirrel/locale/no*/LC_MESSAGES/squirrelmail.mo
%lang(pl) /home/httpd/html/squirrel/locale/pl/LC_MESSAGES/squirrelmail.mo
%lang(pt) /home/httpd/html/squirrel/locale/pt*/LC_MESSAGES/squirrelmail.mo
%lang(ru) /home/httpd/html/squirrel/locale/ru/LC_MESSAGES/squirrelmail.mo
%lang(sr) /home/httpd/html/squirrel/locale/sr/LC_MESSAGES/squirrelmail.mo
%lang(sv) /home/httpd/html/squirrel/locale/sv/LC_MESSAGES/squirrelmail.mo
%lang(tw) /home/httpd/html/squirrel/locale/tw/LC_MESSAGES/squirrelmail.mo
