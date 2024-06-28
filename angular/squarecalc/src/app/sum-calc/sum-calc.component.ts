import { Component } from '@angular/core';

@Component({
  selector: 'app-sum-calc',
  templateUrl: './sum-calc.component.html',
  styleUrl: './sum-calc.component.css'
})
export class SumCalcComponent {
  num1:number = 15
  num2:number = 25
  res:number = 0
  findSum(){
    this.res = (+this.num1) + (+this.num2)
  }
}
