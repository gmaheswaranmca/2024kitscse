import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CalcComponent } from './calc/calc.component';
import { SumCalcComponent } from './sum-calc/sum-calc.component';
import { VendorCreateComponent } from './vendor-create/vendor-create.component';
import { VendorEditComponent } from './vendor-edit/vendor-edit.component';
import { VendorListComponent } from './vendor-list/vendor-list.component';

const routes: Routes = [    
    {path:'calc/square', component:CalcComponent},
    {path:'calc/sum', component:SumCalcComponent},
    {path:'vendors/create', component:VendorCreateComponent},
    {path:'vendors/edit/:id', component:VendorEditComponent},
    {path:'vendors/list', component:VendorListComponent},
    {path:'', component:CalcComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
