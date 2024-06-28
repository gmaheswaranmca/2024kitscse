import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { CalcComponent } from './calc/calc.component';
import { FormsModule } from '@angular/forms';
import { SumCalcComponent } from './sum-calc/sum-calc.component';

@NgModule({
  declarations: [
    AppComponent,
    CalcComponent,
    SumCalcComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
