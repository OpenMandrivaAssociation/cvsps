Name:           cvsps
Version:        2.2b1
Release:        3
Summary:        Patchset tool for CVS
Group:          Development/Other
License:        GPLv3
URL:            http://www.cobite.com/cvsps/
Source0:        http://www.cobite.com/cvsps/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:  zlib-devel
# Requires cvs only with --no-cvs-direct, but I cannot imagine this dep
# being a problem on systems where cvsps will be installed...
Requires:       cvs

%description
CVSps is a program for generating 'patchset' information from a CVS
repository.  A patchset in this case is defined as a set of changes
made to a collection of files, and all committed at the same time
(using a single 'cvs commit' command).  This information is valuable
to seeing the big picture of the evolution of a cvs project.  While
cvs tracks revision information, it is often difficult to see what
changes were committed 'atomically' to the repository.


%prep
%setup -q


%build
CFLAGS="$RPM_OPT_FLAGS" %make


%install
rm -rf $RPM_BUILD_ROOT
install -Dpm 755 cvsps $RPM_BUILD_ROOT%{_bindir}/cvsps
install -Dpm 644 cvsps.1 $RPM_BUILD_ROOT%{_mandir}/man1/cvsps.1


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc CHANGELOG COPYING README merge_utils.sh
%{_bindir}/cvsps
%{_mandir}/man1/cvsps.1*





%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 2.2b1-2mdv2011.0
+ Revision: 610184
- rebuild

* Tue Feb 16 2010 Sandro Cazzaniga <kharec@mandriva.org> 2.2b1-1mdv2010.1
+ Revision: 506775
- fix licence and update to cvsps 2.2b1

* Wed Sep 02 2009 Thierry Vignaud <tv@mandriva.org> 2.1-6mdv2010.0
+ Revision: 425559
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 2.1-5mdv2009.0
+ Revision: 243837
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 2.1-3mdv2008.1
+ Revision: 140717
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Aug 25 2007 Gaëtan Lehmann <glehmann@mandriva.org> 2.1-3mdv2008.0
+ Revision: 71312
- rebuild


* Wed Aug 09 2006 glehmann
+ 08/09/06 19:33:46 (55025)
rebuild

* Sun Jul 30 2006 glehmann
+ 07/30/06 10:22:50 (42682)
Import cvsps

* Wed Sep 07 2005 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 2.1-1mdk
- mandriva contrib

* Fri May 27 2005 Ville Skyttä <ville.skytta at iki.fi> - 2.1-2
- 2.1.

* Sun Mar 20 2005 Ville Skyttä <ville.skytta at iki.fi> - 2.0-0.2.rc1
- Drop 0.fdr and Epoch: 0.

* Sun Sep 14 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:2.0-0.fdr.0.2.rc1
- Remove #---- section markers.

