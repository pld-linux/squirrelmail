Summary:	The SquirrelMail, a WebMail package
Summary(pl):	Wiewórcza Poczta, Poczta przez WWW
Name:		squirrelmail
Version:	1.2.6
Release:	2
License:	GPL
Group:		Applications/Mail
Source0:	http://prdownloads.sf.net/squirrelmail/%{name}-%{version}.tar.bz2
Source1:	http://www.squirrelmail.org/plugins/%{name}_plugins-20010604.tar
Patch0:		squirrelmail-fortune.patch
Patch1:		squirrelmail-ri_once.patch
URL:		http://www.squirrelmail.org/
Requires:	webserver
Requires:	php
Requires:	php-gettext
Requires:	php-pcre
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

%package ispell
Summary:	A squirreel interface to ispel
Summary(pl):	Wiewórczy inerfejs do ispela
Group:		Applications/Mail
Requires:	ispell
Requires:	%{name} = %{version}
Provides:	webmail-spellcheck

%description ispell
This package contains a interface to ispell and it allows you to check
mail against typos and common mistakes

%description ispell -l pl
Pakiet zawiera interfejs do ispela pozwalaj±cy sprawdziæ pocztê pod
k±tem ¼le wpisanych s³ów i ortografi.

%package mailfetch
Summary:	A squirrel pop3 plug-in
Summary(pl):	Wiewiórczy plug-in pop3
Group:		Applications/Mail
Requires:	%{name} = %{version}

%description mailfetch
This package contains a interface to pop3 serwers, it allows you to
fetch mail from this kind of serwers.

%description ispell -l pl
Pakiet zawiera interfejs do serwerów pop3, pozwala ¶ci±gn±c z nich
pocztê za pomoc± us³ugi pop3.

%prep
%setup -q -a1

# List of usefull plugins (ONLY usefull one should be here)
for i in change_pass*tar.gz username*tar.gz abook_take*tar.gz \
	addgraphics*tar.gz attachment_common*tar.gz vacation*tar.gz \
	sqclock*tar.gz retrieveuserdata*tar.gz squirrelspell*tar.gz \
	quicksave*tar.gz printer_friendly*tar.gz password_forget*tar.gz \
	newmail*tar.gz motd*tar.gz mail_fwd*tar.gz mail_fetch*tar.gz \
	gzip*tar.gz fortune*tar.gz auto_cc*tar.gz; do
		tar xfvz $i -C plugins
done

%patch0 -p1
%patch1 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/home/httpd/html/squirrel/{config,data} \
	$RPM_BUILD_ROOT%{_datadir}/docs/squirrel/

gzip -9nf AUTHORS ChangeLog INSTALL README UPGRADE doc/*.txt doc/*.html \
	doc/README* doc/ReleaseNotes/1.2/*

cp -avR * $RPM_BUILD_ROOT/home/httpd/html/squirrel
cd plugins/squirrelspell
cp sqspell_config.dist sqspell_config.php

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz doc/*.gz
%defattr(750,root,http,750)
%attr(730,http,http) /home/httpd/html/squirrel/data/
/home/httpd/html/squirrel/index.php
/home/httpd/html/squirrel/configure
%config(noreplace) /home/httpd/html/squirrel/config/*
/home/httpd/html/squirrel/functions/*
/home/httpd/html/squirrel/help/index.php
%lang(ca) /home/httpd/html/squirrel/help/ca_ES
%lang(cs) /home/httpd/html/squirrel/help/cs_CZ
%lang(en) /home/httpd/html/squirrel/help/en_US
%lang(fi) /home/httpd/html/squirrel/help/fi_FI
%lang(fr) /home/httpd/html/squirrel/help/fr_FR
%lang(it) /home/httpd/html/squirrel/help/it_IT
%lang(ko) /home/httpd/html/squirrel/help/ko_KR
%lang(pl) /home/httpd/html/squirrel/help/pl_PL
%lang(ru) /home/httpd/html/squirrel/help/ru_RU
%lang(sv) /home/httpd/html/squirrel/help/sv_SE
/home/httpd/html/squirrel/images
/home/httpd/html/squirrel/plugins/README.plugins
/home/httpd/html/squirrel/plugins/abook_take
/home/httpd/html/squirrel/plugins/addgraphics
/home/httpd/html/squirrel/plugins/attachment_common
/home/httpd/html/squirrel/plugins/auto_cc
/home/httpd/html/squirrel/plugins/change_pass
/home/httpd/html/squirrel/plugins/fortune
/home/httpd/html/squirrel/plugins/gzip
/home/httpd/html/squirrel/plugins/index.php
/home/httpd/html/squirrel/plugins/mail_fwd
/home/httpd/html/squirrel/plugins/make_archive.pl
/home/httpd/html/squirrel/plugins/motd
/home/httpd/html/squirrel/plugins/newmail
/home/httpd/html/squirrel/plugins/password_forget
/home/httpd/html/squirrel/plugins/printer_friendly
/home/httpd/html/squirrel/plugins/quicksave
/home/httpd/html/squirrel/plugins/retrieveuserdata
/home/httpd/html/squirrel/plugins/sqclock
/home/httpd/html/squirrel/plugins/username
/home/httpd/html/squirrel/plugins/vacation
/home/httpd/html/squirrel/src
/home/httpd/html/squirrel/themes
/home/httpd/html/squirrel/locale/index.php
%dir /home/httpd/html/squirrel/locale
%dir /home/httpd/html/squirrel/locale/[^i]*
%lang(is) %dir /home/httpd/html/squirrel/locale/is_IS/LC_MESSAGES
%lang(it) %dir /home/httpd/html/squirrel/locale/it_IT/LC_MESSAGES
%lang(ca) /home/httpd/html/squirrel/locale/ca_ES/LC_MESSAGES/squirrelmail.mo
%lang(da) /home/httpd/html/squirrel/locale/da_DK/LC_MESSAGES/squirrelmail.mo
%lang(de) /home/httpd/html/squirrel/locale/de_DE/LC_MESSAGES/squirrelmail.mo
%lang(cs) /home/httpd/html/squirrel/locale/cs_CZ/LC_MESSAGES/squirrelmail.mo
%lang(es) /home/httpd/html/squirrel/locale/es_ES/LC_MESSAGES/squirrelmail.mo
%lang(fi) /home/httpd/html/squirrel/locale/fi_FI/LC_MESSAGES/squirrelmail.mo
%lang(fr) /home/httpd/html/squirrel/locale/fr_FR/LC_MESSAGES/squirrelmail.mo
%lang(hr) /home/httpd/html/squirrel/locale/hr_HR/LC_MESSAGES/squirrelmail.mo
%lang(hu) /home/httpd/html/squirrel/locale/hu_HU/LC_MESSAGES/squirrelmail.mo
%lang(is) /home/httpd/html/squirrel/locale/is_IS/LC_MESSAGES/squirrelmail.mo
%lang(it) /home/httpd/html/squirrel/locale/it_IT/LC_MESSAGES/squirrelmail.mo
%lang(ko) /home/httpd/html/squirrel/locale/ko_KR/LC_MESSAGES/squirrelmail.mo
%lang(nl) /home/httpd/html/squirrel/locale/nl_NL/LC_MESSAGES/squirrelmail.mo
%lang(no) /home/httpd/html/squirrel/locale/no*/LC_MESSAGES/squirrelmail.mo
%lang(pl) /home/httpd/html/squirrel/locale/pl_PL/LC_MESSAGES/squirrelmail.mo
%lang(pt) /home/httpd/html/squirrel/locale/pt*/LC_MESSAGES/squirrelmail.mo
%lang(ru) /home/httpd/html/squirrel/locale/ru_RU/LC_MESSAGES/squirrelmail.mo
%lang(sr) /home/httpd/html/squirrel/locale/sr_YU/LC_MESSAGES/squirrelmail.mo
%lang(sv) /home/httpd/html/squirrel/locale/sv_SE/LC_MESSAGES/squirrelmail.mo

%files ispell
%defattr(644,root,root,755)
/home/httpd/html/squirrel/plugins/squirrelspell

%files mailfetch
%defattr(644,root,root,755)
/home/httpd/html/squirrel/plugins/mail_fetch
