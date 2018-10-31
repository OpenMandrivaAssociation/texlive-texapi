# revision 24237
# category Package
# catalog-ctan /macros/generic/texapi
# catalog-date 2011-10-03 08:52:14 +0200
# catalog-license lppl
# catalog-version 1.04
Name:		texlive-texapi
Version:	1.04
Release:	11
Summary:	Macros to write format-independent packages
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/texapi
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texapi.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texapi.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Texapi provides utility macros to write format-independent (and
-aware) packages. It is similar in spirit to the etoolbox,
except that it isn't tied to LaTeX. Tools include: engine and
format detection, expansion control, command definition and
manipulation, various testing macros, string operations, and
highly customizable while and for loops. The package requires
e-TeX (and, should you want to compile its documentation, the
pitex package is also needed).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/texapi/texapi.tex
%doc %{_texmfdistdir}/doc/generic/texapi/README
%doc %{_texmfdistdir}/doc/generic/texapi/texapi-doc.pdf
%doc %{_texmfdistdir}/doc/generic/texapi/texapi-doc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.04-2
+ Revision: 756596
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.04-1
+ Revision: 719675
- texlive-texapi
- texlive-texapi
- texlive-texapi

