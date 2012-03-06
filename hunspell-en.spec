Name: hunspell-en
Summary: English hunspell dictionaries
%define upstreamid 20090216
Version: 0.%{upstreamid}
Release: 7.1%{?dist}
#svn co https://wordlist.svn.sourceforge.net/svnroot/wordlist/trunk wordlist
Source0: wordlist-%{upstreamid}.tar.bz2
Source1: http://en-gb.pyxidium.co.uk/dictionary/en_GB.zip
#See http://mxr.mozilla.org/mozilla/source/extensions/spellcheck/locales/en-US/hunspell/mozilla_words.diff?raw=1
Patch0: mozilla_words.patch
Patch1: en_GB-singleletters.patch
Patch2: en_GB.two_initial_caps.patch
Patch3: en_US-strippedabbrevs.patch
Group: Applications/Text
URL: http://wordlist.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: LGPLv2+ and BSD
BuildArch: noarch
BuildRequires: hunspell, aspell, zip
Requires: hunspell

%description
English (US, UK, etc.) hunspell dictionaries

%prep
%setup -q -n wordlist
%setup -q -T -D -a 1 -n wordlist
%patch0 -p1 -b .mozilla
%patch1 -p1 -b .singleletters
%patch2 -p1 -b .two_initial_cap
%patch3 -p1 -b .strippedabbrevs

%build
make
cd scowl/speller
make hunspell
for i in README_en_CA.txt README_en_US.txt; do
  if ! iconv -f utf-8 -t utf-8 -o /dev/null $i > /dev/null 2>&1; then
    iconv -f ISO-8859-1 -t UTF-8 $i > $i.new
    touch -r $i $i.new
    mv -f $i.new $i
  fi
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p en_*.dic en_*.aff $RPM_BUILD_ROOT/%{_datadir}/myspell
cd scowl/speller
cp -p en_*.dic en_*.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

pushd $RPM_BUILD_ROOT/%{_datadir}/myspell/
en_GB_aliases="en_AG en_AU en_BS en_BW en_BZ en_DK en_GH en_HK en_IE en_IN en_JM en_NA en_NG en_NZ en_SG en_TT en_ZA en_ZW"
for lang in $en_GB_aliases; do
	ln -s en_GB.aff $lang.aff
	ln -s en_GB.dic $lang.dic
done
en_US_aliases="en_PH"
for lang in $en_US_aliases; do
	ln -s en_US.aff $lang.aff
	ln -s en_US.dic $lang.dic
done
popd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README_en_GB.txt scowl/speller/README_en_CA.txt scowl/speller/README_en_US.txt
%{_datadir}/myspell/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.20090216-7.1
- Rebuilt for RHEL 6

* Sat Jul 25 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090216-7
- add extra mozilla REPs

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20090216-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jul 11 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090216-5
- tidy spec

* Fri Jun 12 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090216-4
- extend coverage

* Sat Jun 06 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090216-3
- Change two suspicious words with two initial capitals in en_GB
  from ADte TEirtza to ADTe Teirtza

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20090216-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 16 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090216-1
- fix upstreamed

* Mon Feb 16 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090208-1
- latest version

* Wed Jan 14 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090114-1
- latest version

* Sun Jan 11 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090110-1
- latest version

* Thu Dec 18 2008 Caolan McNamara <caolanm@redhat.com> - 0.20081216-1
- latest version

* Sat Dec 06 2008 Caolan McNamara <caolanm@redhat.com> - 0.20081205-1
- latest version

* Tue Dec 02 2008 Caolan McNamara <caolanm@redhat.com> - 0.20081202-1
- latest version

* Sun Nov 29 2008 Caolan McNamara <caolanm@redhat.com> - 0.20081129-1
- mozilla blog ... webmistresses signature range integrated

* Thu Nov 27 2008 Caolan McNamara <caolanm@redhat.com> - 0.20081127-2
- abbrevs are always stripped out from US/CA dicts
- some single characters are missing from en_GB

* Thu Nov 27 2008 Caolan McNamara <caolanm@redhat.com> - 0.20081127-1
- hardcoded path dropped upstream

* Tue Nov 25 2008 Caolan McNamara <caolanm@redhat.com> - 0.20081124-1
- latest version, i.e +Barack +Obama and co.

* Fri Aug 29 2008 Caolan McNamara <caolanm@redhat.com> - 0.20080829-1
- latest version

* Fri Feb 08 2008 Caolan McNamara <caolanm@redhat.com> - 0.20080207-1
- canonical upstream source

* Thu Feb 07 2008 Caolan McNamara <caolanm@redhat.com> - 0.20061130-5
- apply mozilla word diff

* Tue Jan 15 2008 Caolan McNamara <caolanm@redhat.com> - 0.20061130-4
- clean up spec

* Mon Sep 17 2007 Caolan McNamara <caolanm@redhat.com> - 0.20061130-3
- new varient alias

* Thu Aug 09 2007 Caolan McNamara <caolanm@redhat.com> - 0.20061130-2
- clarify licence

* Fri Jun 01 2007 Caolan McNamara <caolanm@redhat.com> - 0.20061130-1
- update to latest dictionaries

* Thu Feb 08 2007 Caolan McNamara <caolanm@redhat.com> - 0.20040623-2
- update to new spec guidelines

* Thu Dec 07 2006 Caolan McNamara <caolanm@redhat.com> - 0.20040623-1
- initial version
