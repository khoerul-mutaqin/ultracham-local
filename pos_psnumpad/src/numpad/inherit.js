/** @odoo-module */
import { patch } from "@web/core/utils/patch";
import { numpad } from "@point_of_sale/app/generic_components/numpad";
export const DECIMAL = {
    get value() {
        return localization.decimalPoint;
    },
};
export const BACKSPACE = { value: "Backspace", text: "⌫" };
export const ZERO = { value: "0" };
export const DEFAULT_LAST_ROW = [{ value: "-", text: "+/-" }, ZERO, DECIMAL];
export const EMPTY = { value: "" };

export function getButtons(lastRow, rightColumn) {
    return [
        { value: "1" },
        { value: "2" },
        { value: "3" },
        ...(rightColumn ? [rightColumn[0]] : []),
        { value: "4" },
        { value: "5" },
        { value: "6" },
        ...(rightColumn ? [rightColumn[1]] : []),
        { value: "7" },
        { value: "8" },
        { value: "9" },
        ...(rightColumn ? [rightColumn[2]] : []),
        ...lastRow,
        ...(rightColumn ? [rightColumn[3]] : []),
    ];
}

export function enhancedButtons() {
    return getButtons(DEFAULT_LAST_ROW, [
        { value: "+10" },
        { value: "+20" },
        { value: "+50" },
        BACKSPACE,
    ]);
}

patch(numpad.prototype, {
    setup() {
        super.setup(...arguments);
    },
    get buttons() {
        return this.props.buttons || getButtons([DECIMAL, ZERO, BACKSPACE]);
    } 
});
