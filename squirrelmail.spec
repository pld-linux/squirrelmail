# TODO:
# - make separate packages with plugins
#
Summary:	The SquirrelMail, a WebMail package
Summary(pl):	Wiewiórcza Poczta, Poczta przez WWW
Summary(pt_BR):	O SquirrelMail é um webmail
Name:		squirrelmail
Version:	1.4.4
Release:	1
License:	GPL
Group:		Applications/Mail
Source0:	http://dl.sourceforge.net/squirrelmail/%{name}-%{version}.tar.bz2
# Source0-md5:	285b42bec8967b88ef3c083fcad18634
Source1:	%{name}_plugins-20050108.tar
# Source1-md5:	819fa3165bc6ab43c9cdd53addcf340c
%define		_compatibility_version	1.3
Source2:	http://www.squirrelmail.org/plugins/compatibility-%{_compatibility_version}.tar.gz
# Source2-md5:	049c46507ef161ad4ba5f4d4a0b96d09
#%define		_change_passwd_version	4.0
#Source3:	http://www.squirrelmail.org/plugins/change_passwd-%{_change_passwd_version}-1.2.8.tar.gz
## Source3-md5:	22b5ee1698b2e59a88f2150a96ec17f3
%define		_all_locales_date	20050122
Source4:	http://dl.sourceforge.net/squirrelmail/all_locales-%{version}-%{_all_locales_date}.tar.bz2
# Source4-md5:	ec7f97d77c706135571732ac7accf961
Source5:	%{name}.conf
Patch0:		%{name}-config.patch
Patch1:		%{name}-ri_once.patch
Patch2:		%{name}-abook_take.patch
Patch3:		%{name}-addgraphics.patch
Patch4:		%{name}-auto_cc.patch
Patch5:		%{name}-fortune.patch
Patch6:		%{name}-gzip.patch
Patch7:		%{name}-mail_fwd.patch
Patch8:		%{name}-change_pass-i18n.patch
Patch9:		%{name}-change_pass-polish.patch
Patch10:	%{name}-mail_fwd-Makefile.patch
URL:		http://www.squirrelmail.org/
BuildRequires:	gettext-devel
Requires:	php
Requires:	php-gettext
Requires:	php-pcre
Requires:	php-posix
Requires:	php-zlib
Requires:	webserver
Provides:	squirrelmail-compatibility-%{_compatibility_version}
Provides:	webmail
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_squirreldir	%{_datadir}/%{name}
%define		_squirreldata	/var/lib/%{name}

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
Pakiet zawiera Wiewiórcz± Pocztê, system pozwalaj±cy sprawdzaæ pocztê
przez dowoln±, obs³uguj±c± ciasteczka przegl±darkê WWW. Pakiet u¿ywa
wbudowanej w PHP obs³ugi protoko³ów IMAP i SMTP, a serwowane strony
u¿ywaj± tylko HTML 4.0 (bez Javascriptu) po to, ¿eby udostêpniaæ
zasoby na mo¿liwie du¿± ilo¶æ typów przegl±darek http. Pakiet jest
³atwy w instalacji i konfigurowaniu, a tak¿e ma wszystkie obecnie
wymagane cechy dobrego klienta pocztowego jak obs³uga MIME, ksi±¿ka
adresowa i wsparcie dla przechowywania listów w folderach.

%description -l pt_BR
O SquirrelMail é um webmail baseado. Ele inclui suporte em PHP puro
para os protocolos IMAP e SMTP e todas as páginas são montadas em puro
HTML 4.0 (sem nenhum Javascript) para máxima compatibilidade entre
navegadores. Ele possui poucas exigências e é muito fácil de se
configurar e instalar. O SquirrelMail possui todas as funcionalidades
que você poderia desejar em um cliente de e-mail, incluindo um forte
suporte a MIME, livros de endereços e manipulação de pastas.

%package change_pass
Summary:	A squirreel interface to change passwords
Summary(pl):	Wiewiórczy interfejs do zmiany hase³
Group:		Applications/Mail
Requires:	poppassd
Requires:	%{name} = %{version}-%{release}
Requires:	squirrelmail-compatibility-%{_compatibility_version}

%description change_pass
This package contains a interface to change passwords.

%description change_pass -l pl
Ten pakiet zawiera interfejs do zmiany hase³.

%package ispell
Summary:	A squirreel interface to ispel
Summary(pl):	Wiewiórczy inerfejs do ispela
Group:		Applications/Mail
Requires:	ispell
Requires:	%{name} = %{version}-%{release}
Provides:	webmail-spellcheck

%description ispell
This package contains a interface to ispell and it allows you to check
mail against typos and common mistakes

%description ispell -l pl
Pakiet zawiera interfejs do ispella pozwalaj±cy sprawdziæ pocztê pod
k±tem ¼le wpisanych s³ów i ortografii.

%package mail_fwd
Summary:	A squirrel email forwarding plug-in
Summary(pl):	Wtyczka umo¿liwiaj±ca przekierowanie poczty
Group:		Applications/Mail
Requires:	%{name} = %{version}-%{release}

%description mail_fwd
This plug-in allows to set email forwarding.
Note: binary file included in this package must be suid.

%description mail_fwd -l pl
Ta wtyczka pozwala na ustawienie przekierowania poczty.
Uwaga: plik binarny zawarty w tym pakiecie musi mieæ ustawiony bit
suid.

%package mailfetch
Summary:	A squirrel pop3 plug-in
Summary(pl):	Wiewiórcza wtyczka pop3
Group:		Applications/Mail
Requires:	%{name} = %{version}-%{release}

%description mailfetch
This package contains a interface to pop3 serwers, it allows you to
fetch mail from this kind of serwers.

%description mailfetch -l pl
Pakiet zawiera interfejs do serwerów pop3, pozwala ¶ci±gaæ z nich
pocztê za pomoc± us³ugi pop3.

%package newmail
Summary:	A new mail notify plug-in
Summary(pl):	Wtyczka informuj±ca o nowej poczcie
Group:		Applications/Mail
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-ispell = %{version}-%{release}

%description newmail
A Squirrel new mail notify plug-in.

%description newmail -l pl
Wiewiórcza wtyczka informuj±ca o nowej poczcie.

%prep
#%setup -q -a1
%setup -q -a1 -n %{name}-%{version}

# List of useful plugins (ONLY useful ones should be here)
for i in addgraphics*.tar.gz auto_cc*.tar.gz change_pass*.tar.gz \
	gzip*.tar.gz mail_fwd*.tar.gz motd*.tar.gz \
	password_forget*.tar.gz quicksave*.tar.gz retrieveuserdata*.tar.gz \
	username*.tar.gz vacation*.tar.gz; do
		tar -xzf $i -C plugins
done

tar -xzf %{SOURCE2} -C plugins
#tar -xzf %{SOURCE3} -C plugins
tar -xjf %{SOURCE4}

#rm -f plugins/change_passwd/chpasswd
rm -f plugins/mail_fwd/fwdfile/wfwd.o

%patch0 -p1
%patch1 -p1
#%patch2 -p1
#%patch3 -p1
#%patch4 -p1
%patch5 -p1
#%patch6 -p1
#%patch7 -p1
#%patch8 -p1
#%patch9 -p1
%patch10 -p1
%build
%{__make} -C plugins/mail_fwd/fwdfile \
	CFLAGS="%{rpmcflags}" \
	LFLAGS="%{rpmldflags}"

#%{__cc} %{rpmldflags} %{rpmcflags} -Wall -o plugins/change_passwd/chpasswd \
#	plugins/change_passwd/chpasswd.c -lcrypt

cd po
./compilepo pl_PL
cd ..

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_squirreldir}/{config,data},%{_sbindir}} \
	$RPM_BUILD_ROOT{%{_datadir}/docs/squirrel,%{_squirreldata}/{prefs,data}} \
	$RPM_BUILD_ROOT%{_sysconfdir}/%{name} \
	$RPM_BUILD_ROOT%{_sysconfdir}/httpd

install plugins/mail_fwd/fwdfile/wfwd $RPM_BUILD_ROOT%{_sbindir}

install %{SOURCE5} $RPM_BUILD_ROOT%{_sysconfdir}/httpd/%{name}.conf

cp -avR * $RPM_BUILD_ROOT%{_squirreldir}

cd $RPM_BUILD_ROOT
rm -rf `find . -name *.po`
cd -

rm -f $RPM_BUILD_ROOT%{_squirreldir}/plugins/{username/options.php,gzip/setup.php~}

cp $RPM_BUILD_ROOT{%{_squirreldir}/config/config_default.php,%{_sysconfdir}/%{name}/config.php}
ln -sf %{_sysconfdir}/%{name}/config.php $RPM_BUILD_ROOT%{_squirreldir}/config/config.php

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f %{_sysconfdir}/httpd/httpd.conf ] && ! grep -q "^Include.*%{name}.conf" %{_sysconfdir}/httpd/httpd.conf; then
        echo "Include %{_sysconfdir}/httpd/%{name}.conf" >> %{_sysconfdir}/httpd/httpd.conf
elif [ -d %{_sysconfdir}/httpd/httpd.conf ]; then
        ln -sf %{_sysconfdir}/httpd/%{name}.conf %{_sysconfdir}/httpd/httpd.conf/99_%{name}.conf
fi
if [ -f /var/lock/subsys/httpd ]; then
        /usr/sbin/apachectl restart 1>&2
fi

%preun
if [ "$1" = "0" ]; then
        umask 027
        if [ -d %{_sysconfdir}/httpd/httpd.conf ]; then
            rm -f %{_sysconfdir}/httpd/httpd.conf/99_%{name}.conf
        else
                grep -v "^Include.*%{name}.conf" %{_sysconfdir}/httpd/httpd.conf > \
                        %{_sysconfdir}/httpd/httpd.conf.tmp
                mv -f %{_sysconfdir}/httpd/httpd.conf.tmp %{_sysconfdir}/httpd/httpd.conf
                if [ -f /var/lock/subsys/httpd ]; then
                    /usr/sbin/apachectl restart 1>&2
                fi
        fi
fi

%triggerpostun -- squirrelmail < 1.4.3a-5
if [ -f /home/services/httpd/html/squirrel/config/config.php.rpmsave ]; then
	echo "Moving old config file to %{_sysconfdir}/%{name}/config.php"
	mv -f %{_sysconfdir}/%{name}/config.php %{_sysconfdir}/%{name}/config.php.rpmnew
	mv -f /home/services/httpd/html/squirrel/config/config.php.rpmsave \
		%{_sysconfdir}/%{name}/config.php
fi

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README ReleaseNotes UPGRADE doc/*.txt doc/*.html
%doc doc/README* doc/ReleaseNotes/*/*
%dir %{_squirreldir}
%{_squirreldir}/class
%attr(640,root,http) %{_squirreldir}/data/.htaccess
%attr(640,root,http) %{_squirreldir}/data/*
%{_squirreldir}/index.php
%attr(744,root,root) %{_squirreldir}/configure
%attr(750,root,http) %dir %{_squirreldir}/config
%attr(744,root,root) %{_squirreldir}/config/*.pl
%attr(640,root,http) %config(noreplace) %{_squirreldir}/config/*.php
%dir %{_sysconfdir}/%{name}
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/httpd/%{name}.conf
%attr(640,root,http) %config(noreplace) %{_sysconfdir}/%{name}/config.php
%{_squirreldir}/functions
%dir %{_squirreldir}/help
%{_squirreldir}/help/index.php
%{_squirreldir}/help/en_US
%lang(bg) %{_squirreldir}/help/bg_BG
%lang(ca) %{_squirreldir}/help/ca_ES
%lang(cs) %{_squirreldir}/help/cs_CZ
%lang(cy) %{_squirreldir}/help/cy_GB
%lang(da) %{_squirreldir}/help/da_DK
%lang(de) %{_squirreldir}/help/de_DE
%lang(en) %{_squirreldir}/help/en_GB
%lang(es) %{_squirreldir}/help/es_ES
%lang(fi) %{_squirreldir}/help/fi_FI
%lang(fr) %{_squirreldir}/help/fr_FR
%lang(id) %{_squirreldir}/help/id_ID
%lang(it) %{_squirreldir}/help/it_IT
%lang(ja) %{_squirreldir}/help/ja_JP
%lang(ko) %{_squirreldir}/help/ko_KR
%lang(lt) %{_squirreldir}/help/lt_LT
%lang(nl) %{_squirreldir}/help/nl_NL
%lang(pl) %{_squirreldir}/help/pl_PL
%lang(pt) %{_squirreldir}/help/pt_PT
%lang(pt_BR) %{_squirreldir}/help/pt_BR
%lang(ru) %{_squirreldir}/help/ru_RU
%lang(sk) %{_squirreldir}/help/sk_SK
%lang(sl) %{_squirreldir}/help/sl_SI
%lang(sr) %{_squirreldir}/help/sr_YU
%lang(sv) %{_squirreldir}/help/sv_SE
#%lang(th) %{_squirreldir}/help/th_TH
%lang(zh_CN) %{_squirreldir}/help/zh_CN
%{_squirreldir}/images
%{_squirreldir}/include
%dir %{_squirreldir}/locale
%{_squirreldir}/locale/index.php
%{_squirreldir}/locale/timezones.cfg
%lang(ar) %{_squirreldir}/locale/ar
%lang(bg) %{_squirreldir}/locale/bg_BG
%lang(ca) %{_squirreldir}/locale/ca_ES
%lang(da) %{_squirreldir}/locale/da_DK
%lang(de) %{_squirreldir}/locale/de_DE
%lang(cs) %{_squirreldir}/locale/cs_CZ
%lang(cy) %{_squirreldir}/locale/cy_GB
%lang(el) %{_squirreldir}/locale/el_GR
%lang(en) %{_squirreldir}/locale/en_GB
%lang(es) %{_squirreldir}/locale/es_ES
%lang(et) %{_squirreldir}/locale/et_EE
%lang(fi) %{_squirreldir}/locale/fi_FI
%lang(fo) %{_squirreldir}/locale/fo_FO
%lang(fr) %{_squirreldir}/locale/fr_FR
%lang(he) %{_squirreldir}/locale/he_IL
%lang(hr) %{_squirreldir}/locale/hr_HR
%lang(hu) %{_squirreldir}/locale/hu_HU
%lang(id) %{_squirreldir}/locale/id_ID
%lang(is) %{_squirreldir}/locale/is_IS
%lang(it) %{_squirreldir}/locale/it_IT
%lang(ja) %{_squirreldir}/locale/ja_JP
%lang(ko) %{_squirreldir}/locale/ko_KR
%lang(lt) %{_squirreldir}/locale/lt_LT
%lang(ms) %{_squirreldir}/locale/ms_MY
%lang(nb) %{_squirreldir}/locale/nb_NO
%lang(nl) %{_squirreldir}/locale/nl_NL
%lang(nn) %{_squirreldir}/locale/nn_NO
%lang(pl) %{_squirreldir}/locale/pl_PL
%lang(pt) %{_squirreldir}/locale/pt_PT
%lang(pt_BR) %{_squirreldir}/locale/pt_BR
%lang(ro) %{_squirreldir}/locale/ro_RO
%lang(ru) %{_squirreldir}/locale/ru_RU
%lang(sr) %{_squirreldir}/locale/sr_YU
%lang(sv) %{_squirreldir}/locale/sv_SE
%lang(sk) %{_squirreldir}/locale/sk_SK
%lang(sl) %{_squirreldir}/locale/sl_SI
#%lang(th) %{_squirreldir}/locale/th_TH
%lang(tr) %{_squirreldir}/locale/tr_TR
#%lang(uk) %{_squirreldir}/locale/uk_UA
#%lang(vi) %{_squirreldir}/locale/vi_VN
%lang(zh_CN) %{_squirreldir}/locale/zh_CN
%lang(zh_TW) %{_squirreldir}/locale/zh_TW
%dir %{_squirreldir}/plugins
%{_squirreldir}/plugins/README.plugins
%{_squirreldir}/plugins/abook_take
%{_squirreldir}/plugins/addgraphics
%{_squirreldir}/plugins/administrator
%{_squirreldir}/plugins/auto_cc
%{_squirreldir}/plugins/bug_report
%{_squirreldir}/plugins/calendar
%{_squirreldir}/plugins/compatibility
%{_squirreldir}/plugins/delete_move_next
%{_squirreldir}/plugins/filters
%{_squirreldir}/plugins/fortune
%{_squirreldir}/plugins/gzip
%{_squirreldir}/plugins/index.php
%{_squirreldir}/plugins/info
%{_squirreldir}/plugins/listcommands
%{_squirreldir}/plugins/make_archive.pl
%{_squirreldir}/plugins/motd
%{_squirreldir}/plugins/password_forget
%{_squirreldir}/plugins/quicksave
%{_squirreldir}/plugins/retrieveuserdata
%{_squirreldir}/plugins/sent_subfolders
%{_squirreldir}/plugins/spamcop
%{_squirreldir}/plugins/translate
%{_squirreldir}/plugins/username
%{_squirreldir}/plugins/vacation
%{_squirreldir}/src
%{_squirreldir}/themes
%attr(710,root,http) %dir %{_squirreldata}
%attr(730,root,http) %dir %{_squirreldata}/prefs
%attr(730,root,http) %dir %{_squirreldata}/data
# To be removed. Just for compatibility with existing configurations:
%attr(730,root,http) %dir %{_squirreldir}/data

%files change_pass
%defattr(644,root,root,755)
%doc plugins/change_pass/README
%dir %{_squirreldir}/plugins/change_pass
%{_squirreldir}/plugins/change_pass/*.php
%lang(bg) %{_squirreldir}/plugins/change_pass/locale/bg_BG
%lang(de) %{_squirreldir}/plugins/change_pass/locale/de_DE
%lang(es) %{_squirreldir}/plugins/change_pass/locale/es_ES
%lang(fr) %{_squirreldir}/plugins/change_pass/locale/fr_FR
%lang(ja) %{_squirreldir}/plugins/change_pass/locale/ja_JP
%lang(lt) %{_squirreldir}/plugins/change_pass/locale/lt_LT
%lang(pl) %{_squirreldir}/plugins/change_pass/locale/pl_PL
%lang(pt_BR) %{_squirreldir}/plugins/change_pass/locale/pt_BR
%lang(pt) %{_squirreldir}/plugins/change_pass/locale/pt_PT

%files ispell
%defattr(644,root,root,755)
%{_squirreldir}/plugins/squirrelspell

%files mail_fwd
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/wfwd
%doc plugins/mail_fwd/README
%dir %{_squirreldir}/plugins/mail_fwd
%{_squirreldir}/plugins/mail_fwd/[!f]*.php

%files mailfetch
%defattr(644,root,root,755)
%doc plugins/mail_fetch/README
%{_squirreldir}/plugins/mail_fetch/*.php

%files newmail
%defattr(644,root,root,755)
%doc plugins/newmail/{HISTORY,README}
%{_squirreldir}/plugins/newmail/*.php
%{_squirreldir}/plugins/newmail/sounds
