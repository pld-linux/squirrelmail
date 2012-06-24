Summary:	The SquirrelMail, a WebMail package
Summary(pl):	Wiew�rcza Poczta, Poczta przez WWW
Summary(pt_BR):	O SquirrelMail � um webmail
Name:		squirrelmail
Version:	1.2.8
Release:	2
License:	GPL
Group:		Applications/Mail
Source0:	http://prdownloads.sf.net/squirrelmail/%{name}-%{version}.tar.bz2
Source1:	http://www.squirrelmail.org/plugins/%{name}_plugins-20010604.tar
Patch0:		%{name}-fortune.patch
Patch1:		%{name}-ri_once.patch
URL:		http://www.squirrelmail.org/
Requires:	webserver
Requires:	php
Requires:	php-gettext
Requires:	php-pcre
Provides:	webmail
Buildarch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_squirreldir	/home/httpd/html/squirrel

%description
This package contains the Squirrelmail, a webmail system which allows
you check mail by any cookie-aware WWW browser. It includes built-in
pure PHP support for the IMAP and SMTP protocols, and all pages render
in pure HTML 4.0 (with no Javascript) for maximum compatibility across
browsers. It has very few requirements and is very easy to configure
and install. SquirrelMail has a all the functionality you would want
from an email client, including strong MIME support, address books,
and folder manipulation.

%description -l pl
Pakiet zawiera Wiewi�rcz�Poczt�, system pozwalaj�cy sprawdza� poczt�
przez dowoln�, obs�uguj�c� ciasteczka przegl�dark� WWW. Pakiet u�ywa
wbudoewanego w PHP wsparcia do protoko�w IMAP i SMTP, a serwowane
strony u�ywaj� tylko HTML 4.0 (bez Javascript) po to �eby udost�pnia�
zasoby na mo�liwie du�� ilo�� typ� pzregl�darek http. Pakiet jest
�atwy w instalacji i konfigurowaniu, a tak�e ma wszystkie obecnie
wymagane cechy dobrego klienta pocztowego jak wsparcie do MIME,
ksia�ka adresowa i wsparcie do pzrechowywaniu list�w w folderach.

%description -l pt_BR
O SquirrelMail � um webmail baseado. Ele inclui suporte em PHP puro
para os protocolos IMAP e SMTP e todas as p�ginas s�o montadas em puro
HTML 4.0 (sem nenhum Javascript) para m�xima compatibilidade entre
navegadores. Ele possui poucas exig�ncias e � muito f�cil de se
configurar e instalar. O SquirrelMail possui todas as funcionalidades
que voc� poderia desejar em um cliente de e-mail, incluindo um forte
suporte a MIME, livros de endere�os e manipula��o de pastas.

%package ispell
Summary:	A squirreel interface to ispel
Summary(pl):	Wiew�rczy inerfejs do ispela
Group:		Applications/Mail
Requires:	ispell
Requires:	%{name} = %{version}
Provides:	webmail-spellcheck

%description ispell
This package contains a interface to ispell and it allows you to check
mail against typos and common mistakes

%description ispell -l pl
Pakiet zawiera interfejs do ispela pozwalaj�cy sprawdzi� poczt� pod
k�tem �le wpisanych s��w i ortografi.

%package mailfetch
Summary:	A squirrel pop3 plug-in
Summary(pl):	Wiewi�rczy plug-in pop3
Group:		Applications/Mail
Requires:	%{name} = %{version}

%description mailfetch
This package contains a interface to pop3 serwers, it allows you to
fetch mail from this kind of serwers.

%description mailfetch -l pl
Pakiet zawiera interfejs do serwer�w pop3, pozwala �ci�gn�c z nich
poczt� za pomoc� us�ugi pop3.

%prep
%setup -q -a1

# List of usefull plugins (ONLY usefull one should be here)
for i in abook_take*tar.gz addgraphics*tar.gz attachment_common*tar.gz \
	auto_cc*tar.gz change_pass*tar.gz fortune*tar.gz gzip*tar.gz \
	mail_fwd*tar.gz motd*tar.gz password_forget*tar.gz username*tar.gz \
	printer_friendly*tar.gz quicksave*tar.gz retrieveuserdata*tar.gz \
	sqclock*tar.gz vacation*tar.gz; do
		tar xfvz $i -C plugins
done

%patch0 -p1
%patch1 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_squirreldir}/{config,data} \
	$RPM_BUILD_ROOT%{_datadir}/docs/squirrel/

cp -avR * $RPM_BUILD_ROOT%{_squirreldir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog INSTALL README UPGRADE doc/*.txt doc/*.html
%doc doc/README* doc/ReleaseNotes/1.2/*
%defattr(750,root,http,750)
%attr(730,http,http) %{_squirreldir}/data/
%{_squirreldir}/index.php
%{_squirreldir}/configure
%attr(640,root,http) %config(noreplace) %{_squirreldir}/config/*
%{_squirreldir}/functions/*
%{_squirreldir}/help/index.php
%lang(ca) %{_squirreldir}/help/ca_ES
%lang(cs) %{_squirreldir}/help/cs_CZ
%{_squirreldir}/help/en_US
%lang(fi) %{_squirreldir}/help/fi_FI
%lang(fr) %{_squirreldir}/help/fr_FR
%lang(it) %{_squirreldir}/help/it_IT
%lang(ko) %{_squirreldir}/help/ko_KR
%lang(pl) %{_squirreldir}/help/pl_PL
%lang(ru) %{_squirreldir}/help/ru_RU
%lang(sv) %{_squirreldir}/help/sv_SE
%{_squirreldir}/images
%{_squirreldir}/plugins/README.plugins
%{_squirreldir}/plugins/abook_take
%{_squirreldir}/plugins/addgraphics
%{_squirreldir}/plugins/attachment_common
%{_squirreldir}/plugins/auto_cc
%{_squirreldir}/plugins/change_pass
%{_squirreldir}/plugins/fortune
%{_squirreldir}/plugins/gzip
%{_squirreldir}/plugins/index.php
%{_squirreldir}/plugins/mail_fwd
%{_squirreldir}/plugins/make_archive.pl
%{_squirreldir}/plugins/motd
%{_squirreldir}/plugins/newmail
%{_squirreldir}/plugins/password_forget
%{_squirreldir}/plugins/printer_friendly
%{_squirreldir}/plugins/quicksave
%{_squirreldir}/plugins/retrieveuserdata
%{_squirreldir}/plugins/sqclock
%{_squirreldir}/plugins/username
%{_squirreldir}/plugins/vacation
%{_squirreldir}/src
%{_squirreldir}/themes
%{_squirreldir}/locale/index.php
%dir %{_squirreldir}/locale
%dir %{_squirreldir}/locale/[^i]*
%lang(is) %dir %{_squirreldir}/locale/is_IS/LC_MESSAGES
%lang(it) %dir %{_squirreldir}/locale/it_IT/LC_MESSAGES
%lang(ca) %{_squirreldir}/locale/ca_ES/LC_MESSAGES/squirrelmail.mo
%lang(da) %{_squirreldir}/locale/da_DK/LC_MESSAGES/squirrelmail.mo
%lang(de) %{_squirreldir}/locale/de_DE/LC_MESSAGES/squirrelmail.mo
%lang(cs) %{_squirreldir}/locale/cs_CZ/LC_MESSAGES/squirrelmail.mo
%lang(es) %{_squirreldir}/locale/es_ES/LC_MESSAGES/squirrelmail.mo
%lang(fi) %{_squirreldir}/locale/fi_FI/LC_MESSAGES/squirrelmail.mo
%lang(fr) %{_squirreldir}/locale/fr_FR/LC_MESSAGES/squirrelmail.mo
%lang(hr) %{_squirreldir}/locale/hr_HR/LC_MESSAGES/squirrelmail.mo
%lang(hu) %{_squirreldir}/locale/hu_HU/LC_MESSAGES/squirrelmail.mo
%lang(is) %{_squirreldir}/locale/is_IS/LC_MESSAGES/squirrelmail.mo
%lang(it) %{_squirreldir}/locale/it_IT/LC_MESSAGES/squirrelmail.mo
%lang(ko) %{_squirreldir}/locale/ko_KR/LC_MESSAGES/squirrelmail.mo
%lang(nl) %{_squirreldir}/locale/nl_NL/LC_MESSAGES/squirrelmail.mo
%lang(no) %{_squirreldir}/locale/no*/LC_MESSAGES/squirrelmail.mo
%lang(pl) %{_squirreldir}/locale/pl_PL/LC_MESSAGES/squirrelmail.mo
%lang(pt) %{_squirreldir}/locale/pt_PT/LC_MESSAGES/squirrelmail.mo
%lang(pt_BR) %{_squirreldir}/locale/pt_BR/LC_MESSAGES/squirrelmail.mo
%lang(ru) %{_squirreldir}/locale/ru_RU/LC_MESSAGES/squirrelmail.mo
%lang(sr) %{_squirreldir}/locale/sr_YU/LC_MESSAGES/squirrelmail.mo
%lang(sv) %{_squirreldir}/locale/sv_SE/LC_MESSAGES/squirrelmail.mo

%files ispell
%defattr(644,root,root,755)
%{_squirreldir}/plugins/squirrelspell

%files mailfetch
%defattr(644,root,root,755)
%{_squirreldir}/plugins/mail_fetch
