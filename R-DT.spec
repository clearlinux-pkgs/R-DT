#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v7
# autospec commit: f56f1fa
#
Name     : R-DT
Version  : 0.33
Release  : 81
URL      : https://cran.r-project.org/src/contrib/DT_0.33.tar.gz
Source0  : https://cran.r-project.org/src/contrib/DT_0.33.tar.gz
Summary  : A Wrapper of the JavaScript Library 'DataTables'
Group    : Development/Tools
License  : Apache-2.0 GPL-3.0 MIT
Requires: R-DT-license = %{version}-%{release}
Requires: R-crosstalk
Requires: R-htmltools
Requires: R-htmlwidgets
Requires: R-httpuv
Requires: R-jquerylib
Requires: R-jsonlite
Requires: R-magrittr
Requires: R-promises
BuildRequires : R-crosstalk
BuildRequires : R-htmltools
BuildRequires : R-htmlwidgets
BuildRequires : R-httpuv
BuildRequires : R-jquerylib
BuildRequires : R-jsonlite
BuildRequires : R-magrittr
BuildRequires : R-promises
BuildRequires : buildreq-R

%description
JavaScript library 'DataTables' (typically via R Markdown or Shiny). The
    'DataTables' library has been included in this R package. The package name
    'DT' is an abbreviation of 'DataTables'.

%package license
Summary: license components for the R-DT package.
Group: Default

%description license
license components for the R-DT package.


%prep
%setup -q -n DT
pushd ..
cp -a DT buildavx2
popd
pushd ..
cp -a DT buildavx512
popd
pushd ..
cp -a DT buildapx
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1712328129

%install
export SOURCE_DATE_EPOCH=1712328129
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/R-DT
cp %{_builddir}/DT/LICENSE %{buildroot}/usr/share/package-licenses/R-DT/94a81b4765e1de991b3e35b7b41ef2ad3e67087d || :
cp %{_builddir}/DT/inst/htmlwidgets/lib/datatables/license.txt %{buildroot}/usr/share/package-licenses/R-DT/c2dcfeb8923d23301f9b527b95d8884ab1d74ba7 || :
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -mapxf -mavx10.1 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -mapxf -mavx10.1 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-va/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py apx %{buildroot}-va %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/DT/DESCRIPTION
/usr/lib64/R/library/DT/INDEX
/usr/lib64/R/library/DT/LICENSE
/usr/lib64/R/library/DT/Meta/Rd.rds
/usr/lib64/R/library/DT/Meta/features.rds
/usr/lib64/R/library/DT/Meta/hsearch.rds
/usr/lib64/R/library/DT/Meta/links.rds
/usr/lib64/R/library/DT/Meta/nsInfo.rds
/usr/lib64/R/library/DT/Meta/package.rds
/usr/lib64/R/library/DT/Meta/vignette.rds
/usr/lib64/R/library/DT/NAMESPACE
/usr/lib64/R/library/DT/NEWS.Rd
/usr/lib64/R/library/DT/R/DT
/usr/lib64/R/library/DT/R/DT.rdb
/usr/lib64/R/library/DT/R/DT.rdx
/usr/lib64/R/library/DT/doc/DT.Rmd
/usr/lib64/R/library/DT/doc/DT.html
/usr/lib64/R/library/DT/doc/index.html
/usr/lib64/R/library/DT/examples/DT-click/DESCRIPTION
/usr/lib64/R/library/DT/examples/DT-click/Readme.md
/usr/lib64/R/library/DT/examples/DT-click/rsconnect/shinyapps.io/yihui/DT-click.dcf
/usr/lib64/R/library/DT/examples/DT-click/server.R
/usr/lib64/R/library/DT/examples/DT-click/ui.R
/usr/lib64/R/library/DT/examples/DT-crosstalk/plotly-persist.R
/usr/lib64/R/library/DT/examples/DT-deleteRows/DESCRIPTION
/usr/lib64/R/library/DT/examples/DT-deleteRows/Readme.md
/usr/lib64/R/library/DT/examples/DT-deleteRows/server.R
/usr/lib64/R/library/DT/examples/DT-deleteRows/ui.R
/usr/lib64/R/library/DT/examples/DT-edit/DESCRIPTION
/usr/lib64/R/library/DT/examples/DT-edit/Readme.md
/usr/lib64/R/library/DT/examples/DT-edit/app.R
/usr/lib64/R/library/DT/examples/DT-edit/rsconnect/shinyapps.io/yihui/DT-edit.dcf
/usr/lib64/R/library/DT/examples/DT-filter/DESCRIPTION
/usr/lib64/R/library/DT/examples/DT-filter/Readme.md
/usr/lib64/R/library/DT/examples/DT-filter/rsconnect/shinyapps.io/yihui/DT-filter.dcf
/usr/lib64/R/library/DT/examples/DT-filter/server.R
/usr/lib64/R/library/DT/examples/DT-filter/ui.R
/usr/lib64/R/library/DT/examples/DT-info/DESCRIPTION
/usr/lib64/R/library/DT/examples/DT-info/Readme.md
/usr/lib64/R/library/DT/examples/DT-info/rsconnect/shinyapps.io/yihui/DT-info.dcf
/usr/lib64/R/library/DT/examples/DT-info/server.R
/usr/lib64/R/library/DT/examples/DT-info/ui.R
/usr/lib64/R/library/DT/examples/DT-proxy/DESCRIPTION
/usr/lib64/R/library/DT/examples/DT-proxy/Readme.md
/usr/lib64/R/library/DT/examples/DT-proxy/rsconnect/shinyapps.io/yihui/DT-proxy.dcf
/usr/lib64/R/library/DT/examples/DT-proxy/server.R
/usr/lib64/R/library/DT/examples/DT-proxy/ui.R
/usr/lib64/R/library/DT/examples/DT-radio/DESCRIPTION
/usr/lib64/R/library/DT/examples/DT-radio/Readme.md
/usr/lib64/R/library/DT/examples/DT-radio/app.R
/usr/lib64/R/library/DT/examples/DT-radio/rsconnect/shinyapps.io/yihui/DT-radio.dcf
/usr/lib64/R/library/DT/examples/DT-reload/app.R
/usr/lib64/R/library/DT/examples/DT-rows/DESCRIPTION
/usr/lib64/R/library/DT/examples/DT-rows/Readme.md
/usr/lib64/R/library/DT/examples/DT-rows/rsconnect/shinyapps.io/yihui/DT-rows.dcf
/usr/lib64/R/library/DT/examples/DT-rows/server.R
/usr/lib64/R/library/DT/examples/DT-rows/ui.R
/usr/lib64/R/library/DT/examples/DT-scroller/DESCRIPTION
/usr/lib64/R/library/DT/examples/DT-scroller/Readme.md
/usr/lib64/R/library/DT/examples/DT-scroller/rsconnect/shinyapps.io/yihui/DT-scroller.dcf
/usr/lib64/R/library/DT/examples/DT-scroller/server.R
/usr/lib64/R/library/DT/examples/DT-scroller/ui.R
/usr/lib64/R/library/DT/examples/DT-scroller/www/large.txt
/usr/lib64/R/library/DT/examples/DT-searchExact/DESCRIPTION
/usr/lib64/R/library/DT/examples/DT-searchExact/Readme.md
/usr/lib64/R/library/DT/examples/DT-searchExact/server.R
/usr/lib64/R/library/DT/examples/DT-searchExact/ui.R
/usr/lib64/R/library/DT/examples/DT-selection/DESCRIPTION
/usr/lib64/R/library/DT/examples/DT-selection/Readme.md
/usr/lib64/R/library/DT/examples/DT-selection/rsconnect/shinyapps.io/yihui/DT-selection.dcf
/usr/lib64/R/library/DT/examples/DT-selection/server.R
/usr/lib64/R/library/DT/examples/DT-selection/ui.R
/usr/lib64/R/library/DT/examples/DT-shiny/server.R
/usr/lib64/R/library/DT/examples/DT-shiny/ui.R
/usr/lib64/R/library/DT/examples/DT-updateFilters/DESCRIPTION
/usr/lib64/R/library/DT/examples/DT-updateFilters/README.md
/usr/lib64/R/library/DT/examples/DT-updateFilters/app.R
/usr/lib64/R/library/DT/examples/ajax-shiny.R
/usr/lib64/R/library/DT/examples/datatable.R
/usr/lib64/R/library/DT/help/AnIndex
/usr/lib64/R/library/DT/help/DT.rdb
/usr/lib64/R/library/DT/help/DT.rdx
/usr/lib64/R/library/DT/help/aliases.rds
/usr/lib64/R/library/DT/help/paths.rds
/usr/lib64/R/library/DT/html/00Index.html
/usr/lib64/R/library/DT/html/R.css
/usr/lib64/R/library/DT/htmlwidgets/css/datatables-crosstalk.css
/usr/lib64/R/library/DT/htmlwidgets/datatables.js
/usr/lib64/R/library/DT/htmlwidgets/datatables.yaml
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/AutoFill/css/autoFill.bootstrap.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/AutoFill/css/autoFill.bootstrap4.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/AutoFill/css/autoFill.bootstrap5.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/AutoFill/css/autoFill.bulma.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/AutoFill/css/autoFill.dataTables.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/AutoFill/css/autoFill.foundation.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/AutoFill/css/autoFill.jqueryui.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/AutoFill/css/autoFill.semanticui.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/AutoFill/js/autoFill.bootstrap.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/AutoFill/js/autoFill.bootstrap4.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/AutoFill/js/autoFill.bootstrap5.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/AutoFill/js/autoFill.bulma.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/AutoFill/js/autoFill.dataTables.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/AutoFill/js/autoFill.foundation.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/AutoFill/js/autoFill.jqueryui.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/AutoFill/js/autoFill.semanticui.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/AutoFill/js/dataTables.autoFill.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/Buttons/css/buttons.bootstrap.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/Buttons/css/buttons.bootstrap4.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/Buttons/css/buttons.bootstrap5.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/Buttons/css/buttons.bulma.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/Buttons/css/buttons.dataTables.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/Buttons/css/buttons.foundation.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/Buttons/css/buttons.jqueryui.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/Buttons/css/buttons.semanticui.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/Buttons/js/buttons.bootstrap.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/Buttons/js/buttons.bootstrap4.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/Buttons/js/buttons.bootstrap5.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/Buttons/js/buttons.bulma.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/Buttons/js/buttons.colVis.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/Buttons/js/buttons.dataTables.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/Buttons/js/buttons.foundation.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/Buttons/js/buttons.html5.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/Buttons/js/buttons.jqueryui.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/Buttons/js/buttons.print.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/Buttons/js/buttons.semanticui.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/Buttons/js/dataTables.buttons.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/Buttons/js/jszip.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/Buttons/js/pdfmake.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/Buttons/js/vfs_fonts.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/ColReorder/css/colReorder.bootstrap.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/ColReorder/css/colReorder.bootstrap4.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/ColReorder/css/colReorder.bootstrap5.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/ColReorder/css/colReorder.bulma.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/ColReorder/css/colReorder.dataTables.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/ColReorder/css/colReorder.foundation.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/ColReorder/css/colReorder.jqueryui.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/ColReorder/css/colReorder.semanticui.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/ColReorder/js/colReorder.bootstrap.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/ColReorder/js/colReorder.bootstrap4.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/ColReorder/js/colReorder.bootstrap5.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/ColReorder/js/colReorder.bulma.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/ColReorder/js/colReorder.dataTables.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/ColReorder/js/colReorder.foundation.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/ColReorder/js/colReorder.jqueryui.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/ColReorder/js/colReorder.semanticui.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/ColReorder/js/dataTables.colReorder.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/DateTime/css/dataTables.dateTime.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/DateTime/js/dataTables.dateTime.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/FixedColumns/css/fixedColumns.bootstrap.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/FixedColumns/css/fixedColumns.bootstrap4.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/FixedColumns/css/fixedColumns.bootstrap5.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/FixedColumns/css/fixedColumns.bulma.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/FixedColumns/css/fixedColumns.dataTables.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/FixedColumns/css/fixedColumns.foundation.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/FixedColumns/css/fixedColumns.jqueryui.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/FixedColumns/css/fixedColumns.semanticui.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/FixedColumns/js/dataTables.fixedColumns.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/FixedColumns/js/fixedColumns.bootstrap.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/FixedColumns/js/fixedColumns.bootstrap4.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/FixedColumns/js/fixedColumns.bootstrap5.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/FixedColumns/js/fixedColumns.bulma.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/FixedColumns/js/fixedColumns.dataTables.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/FixedColumns/js/fixedColumns.foundation.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/FixedColumns/js/fixedColumns.jqueryui.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/FixedColumns/js/fixedColumns.semanticui.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/FixedHeader/css/fixedHeader.bootstrap.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/FixedHeader/css/fixedHeader.bootstrap4.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/FixedHeader/css/fixedHeader.bootstrap5.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/FixedHeader/css/fixedHeader.bulma.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/FixedHeader/css/fixedHeader.dataTables.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/FixedHeader/css/fixedHeader.foundation.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/FixedHeader/css/fixedHeader.jqueryui.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/FixedHeader/css/fixedHeader.semanticui.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/FixedHeader/js/dataTables.fixedHeader.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/FixedHeader/js/fixedHeader.bootstrap.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/FixedHeader/js/fixedHeader.bootstrap4.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/FixedHeader/js/fixedHeader.bootstrap5.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/FixedHeader/js/fixedHeader.bulma.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/FixedHeader/js/fixedHeader.dataTables.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/FixedHeader/js/fixedHeader.foundation.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/FixedHeader/js/fixedHeader.jqueryui.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/FixedHeader/js/fixedHeader.semanticui.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/KeyTable/css/keyTable.bootstrap.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/KeyTable/css/keyTable.bootstrap4.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/KeyTable/css/keyTable.bootstrap5.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/KeyTable/css/keyTable.bulma.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/KeyTable/css/keyTable.dataTables.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/KeyTable/css/keyTable.foundation.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/KeyTable/css/keyTable.jqueryui.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/KeyTable/css/keyTable.semanticui.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/KeyTable/js/dataTables.keyTable.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/KeyTable/js/keyTable.bootstrap.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/KeyTable/js/keyTable.bootstrap4.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/KeyTable/js/keyTable.bootstrap5.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/KeyTable/js/keyTable.bulma.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/KeyTable/js/keyTable.dataTables.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/KeyTable/js/keyTable.foundation.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/KeyTable/js/keyTable.jqueryui.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/KeyTable/js/keyTable.semanticui.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/Responsive/css/responsive.bootstrap.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/Responsive/css/responsive.bootstrap4.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/Responsive/css/responsive.bootstrap5.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/Responsive/css/responsive.bulma.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/Responsive/css/responsive.dataTables.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/Responsive/css/responsive.foundation.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/Responsive/css/responsive.jqueryui.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/Responsive/css/responsive.semanticui.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/Responsive/js/dataTables.responsive.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/Responsive/js/responsive.bootstrap.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/Responsive/js/responsive.bootstrap4.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/Responsive/js/responsive.bootstrap5.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/Responsive/js/responsive.bulma.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/Responsive/js/responsive.dataTables.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/Responsive/js/responsive.foundation.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/Responsive/js/responsive.jqueryui.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/Responsive/js/responsive.semanticui.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/RowGroup/css/rowGroup.bootstrap.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/RowGroup/css/rowGroup.bootstrap4.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/RowGroup/css/rowGroup.bootstrap5.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/RowGroup/css/rowGroup.bulma.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/RowGroup/css/rowGroup.dataTables.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/RowGroup/css/rowGroup.foundation.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/RowGroup/css/rowGroup.jqueryui.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/RowGroup/css/rowGroup.semanticui.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/RowGroup/js/dataTables.rowGroup.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/RowGroup/js/rowGroup.bootstrap.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/RowGroup/js/rowGroup.bootstrap4.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/RowGroup/js/rowGroup.bootstrap5.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/RowGroup/js/rowGroup.bulma.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/RowGroup/js/rowGroup.dataTables.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/RowGroup/js/rowGroup.foundation.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/RowGroup/js/rowGroup.jqueryui.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/RowGroup/js/rowGroup.semanticui.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/RowReorder/css/rowReorder.bootstrap.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/RowReorder/css/rowReorder.bootstrap4.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/RowReorder/css/rowReorder.bootstrap5.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/RowReorder/css/rowReorder.bulma.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/RowReorder/css/rowReorder.dataTables.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/RowReorder/css/rowReorder.foundation.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/RowReorder/css/rowReorder.jqueryui.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/RowReorder/css/rowReorder.semanticui.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/RowReorder/js/dataTables.rowReorder.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/RowReorder/js/rowReorder.bootstrap.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/RowReorder/js/rowReorder.bootstrap4.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/RowReorder/js/rowReorder.bootstrap5.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/RowReorder/js/rowReorder.bulma.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/RowReorder/js/rowReorder.dataTables.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/RowReorder/js/rowReorder.foundation.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/RowReorder/js/rowReorder.jqueryui.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/RowReorder/js/rowReorder.semanticui.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/Scroller/css/scroller.bootstrap.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/Scroller/css/scroller.bootstrap4.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/Scroller/css/scroller.bootstrap5.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/Scroller/css/scroller.bulma.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/Scroller/css/scroller.dataTables.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/Scroller/css/scroller.foundation.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/Scroller/css/scroller.jqueryui.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/Scroller/css/scroller.semanticui.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/Scroller/js/dataTables.scroller.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/Scroller/js/scroller.bootstrap.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/Scroller/js/scroller.bootstrap4.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/Scroller/js/scroller.bootstrap5.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/Scroller/js/scroller.bulma.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/Scroller/js/scroller.dataTables.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/Scroller/js/scroller.foundation.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/Scroller/js/scroller.jqueryui.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/Scroller/js/scroller.semanticui.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/SearchBuilder/css/searchBuilder.bootstrap.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/SearchBuilder/css/searchBuilder.bootstrap4.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/SearchBuilder/css/searchBuilder.bootstrap5.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/SearchBuilder/css/searchBuilder.bulma.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/SearchBuilder/css/searchBuilder.dataTables.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/SearchBuilder/css/searchBuilder.foundation.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/SearchBuilder/css/searchBuilder.jqueryui.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/SearchBuilder/css/searchBuilder.semanticui.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/SearchBuilder/js/dataTables.searchBuilder.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/SearchBuilder/js/searchBuilder.bootstrap.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/SearchBuilder/js/searchBuilder.bootstrap4.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/SearchBuilder/js/searchBuilder.bootstrap5.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/SearchBuilder/js/searchBuilder.bulma.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/SearchBuilder/js/searchBuilder.dataTables.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/SearchBuilder/js/searchBuilder.foundation.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/SearchBuilder/js/searchBuilder.jqueryui.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/SearchBuilder/js/searchBuilder.semanticui.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/SearchPanes/css/searchPanes.bootstrap.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/SearchPanes/css/searchPanes.bootstrap4.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/SearchPanes/css/searchPanes.bootstrap5.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/SearchPanes/css/searchPanes.bulma.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/SearchPanes/css/searchPanes.dataTables.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/SearchPanes/css/searchPanes.foundation.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/SearchPanes/css/searchPanes.jqueryui.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/SearchPanes/css/searchPanes.semanticui.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/SearchPanes/js/dataTables.searchPanes.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/SearchPanes/js/searchPanes.bootstrap.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/SearchPanes/js/searchPanes.bootstrap4.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/SearchPanes/js/searchPanes.bootstrap5.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/SearchPanes/js/searchPanes.bulma.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/SearchPanes/js/searchPanes.dataTables.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/SearchPanes/js/searchPanes.foundation.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/SearchPanes/js/searchPanes.jqueryui.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/SearchPanes/js/searchPanes.semanticui.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/Select/css/select.bootstrap.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/Select/css/select.bootstrap4.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/Select/css/select.bootstrap5.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/Select/css/select.bulma.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/Select/css/select.dataTables.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/Select/css/select.foundation.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/Select/css/select.jqueryui.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/Select/css/select.semanticui.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/Select/js/dataTables.select.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/Select/js/select.bootstrap.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/Select/js/select.bootstrap4.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/Select/js/select.bootstrap5.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/Select/js/select.bulma.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/Select/js/select.dataTables.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/Select/js/select.foundation.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/Select/js/select.jqueryui.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/Select/js/select.semanticui.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/StateRestore/css/stateRestore.bootstrap.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/StateRestore/css/stateRestore.bootstrap4.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/StateRestore/css/stateRestore.bootstrap5.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/StateRestore/css/stateRestore.bulma.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/StateRestore/css/stateRestore.dataTables.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/StateRestore/css/stateRestore.foundation.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/StateRestore/css/stateRestore.jqueryui.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/StateRestore/css/stateRestore.semanticui.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/StateRestore/js/dataTables.stateRestore.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/StateRestore/js/stateRestore.bootstrap.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/StateRestore/js/stateRestore.bootstrap4.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/StateRestore/js/stateRestore.bootstrap5.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/StateRestore/js/stateRestore.bulma.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/StateRestore/js/stateRestore.dataTables.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/StateRestore/js/stateRestore.foundation.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/StateRestore/js/stateRestore.jqueryui.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-extensions/StateRestore/js/stateRestore.semanticui.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-plugins/dataRender/ellipsis/source.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-plugins/features/scrollResize/source.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-plugins/features/searchHighlight/jquery.highlight.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-plugins/features/searchHighlight/source.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-plugins/features/searchHighlight/source.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-plugins/filtering/accent-neutralise/source.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-plugins/filtering/diacritics-neutralise/source.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-plugins/pagination/ellipses/source.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-plugins/pagination/extjs/source.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-plugins/pagination/four_button/source.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-plugins/pagination/full_numbers_no_ellipses/source.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-plugins/pagination/input/source.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-plugins/pagination/scrolling/source.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-plugins/pagination/select/source.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-plugins/pagination/simple_incremental_bootstrap/source.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-plugins/pagination/simple_numbers_no_ellipses/source.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables-plugins/sorting/natural/source.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables/css/dataTables.bootstrap.extra.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables/css/dataTables.bootstrap.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables/css/dataTables.bootstrap4.extra.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables/css/dataTables.bootstrap4.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables/css/dataTables.bootstrap5.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables/css/dataTables.bulma.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables/css/dataTables.foundation.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables/css/dataTables.jqueryui.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables/css/dataTables.semanticui.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables/css/jquery.dataTables.extra.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables/css/jquery.dataTables.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables/js/dataTables.bootstrap.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables/js/dataTables.bootstrap4.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables/js/dataTables.bootstrap5.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables/js/dataTables.bulma.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables/js/dataTables.dataTables.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables/js/dataTables.foundation.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables/js/dataTables.jqueryui.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables/js/dataTables.semanticui.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables/js/jquery.dataTables.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/datatables/license.txt
/usr/lib64/R/library/DT/htmlwidgets/lib/nouislider/jquery.nouislider.min.css
/usr/lib64/R/library/DT/htmlwidgets/lib/nouislider/jquery.nouislider.min.js
/usr/lib64/R/library/DT/htmlwidgets/lib/selectize/selectize.bootstrap3.css
/usr/lib64/R/library/DT/htmlwidgets/lib/selectize/selectize.min.js
/usr/lib64/R/library/DT/tests/test-all.R
/usr/lib64/R/library/DT/tests/testit/test-datatables.R
/usr/lib64/R/library/DT/tests/testit/test-format.R
/usr/lib64/R/library/DT/tests/testit/test-search.R
/usr/lib64/R/library/DT/tests/testit/test-searchbuilder.R
/usr/lib64/R/library/DT/tests/testit/test-sort.R
/usr/lib64/R/library/DT/tests/testit/test-utils.R

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/R-DT/94a81b4765e1de991b3e35b7b41ef2ad3e67087d
/usr/share/package-licenses/R-DT/c2dcfeb8923d23301f9b527b95d8884ab1d74ba7
