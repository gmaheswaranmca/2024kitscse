import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SumCalcComponent } from './sum-calc.component';

describe('SumCalcComponent', () => {
  let component: SumCalcComponent;
  let fixture: ComponentFixture<SumCalcComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [SumCalcComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SumCalcComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
