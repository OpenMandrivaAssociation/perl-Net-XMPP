%define module	Net-XMPP
%define name	perl-%{module}
%define version 1.02

Name:		%{name}
Version:	%{version}
Release:	%mkrel 7
Summary:	XMPP Perl Library
License:	GPL or Artistic
Group:		Development/Perl
Url:            http://search.cpan.org/dist/%{module}/
Source:         http://www.cpan.org/modules/by-module/Net/%{module}-%{version}.tar.bz2
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(XML::Stream)
BuildArch:	    noarch
BuildRoot:	    %{_tmppath}/%{name}-%{version}

%description
Net::XMPP is a convenient tool to use for any perl script that would
like to utilize the XMPP Instant Messaging protocol.  While not a
client in and of itself, it provides all of the necessary back-end
functions to make a CGI client or command-line perl client feasible 
and easy to use.  Net::XMPP is a wrapper around the rest of the
official Net::XMPP::xxxxxx packages.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build CFLAGS="%{optflags}"

%check
./Build test

%install
rm -rf %{buildroot}
./Build install destdir=%{buildroot}

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES README
%{perl_vendorlib}/Net
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.02-7mdv2012.0
+ Revision: 765539
- rebuilt for perl-5.14.2
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.02-5
+ Revision: 667282
- mass rebuild

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.02-4mdv2011.0
+ Revision: 426560
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.02-3mdv2009.1
+ Revision: 351776
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.02-2mdv2009.0
+ Revision: 223930
- rebuild

* Wed Jan 02 2008 Olivier Blin <blino@mandriva.org> 1.02-1mdv2008.1
+ Revision: 140694
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Jul 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.02-1mdv2008.0
+ Revision: 46594
- switch to Module::Build
- update to new version 1.02


* Mon May 29 2006 Anssi Hannula <anssi@mandriva.org> 1.0-2mdv2007.0
- %%mkrel
- use better source url

* Wed Sep 21 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.0-1mdk
- first mdk release (TODO: fix tests)

