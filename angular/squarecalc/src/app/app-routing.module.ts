import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CalcComponent } from './calc/calc.component';
import { SumCalcComponent } from './sum-calc/sum-calc.component';

const routes: Routes = [    
    {path:'calc/square', component:CalcComponent},
    {path:'calc/sum', component:SumCalcComponent},
    {path:'', component:CalcComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
